from flask import Flask, request, render_template, redirect, url_for, session
import threading

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Global game state
game_state = {
    'boss_hp': 100,
    'players': {},  # player_id -> player_name
    'turn': None,
    'messages': []
}

lock = threading.Lock()

def broadcast_message(msg):
    with lock:
        game_state['messages'].append(msg)
        if len(game_state['messages']) > 20:
            game_state['messages'].pop(0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'player_id' not in session:
        # Assign player ID
        with lock:
            player_id = len(game_state['players']) + 1
            session['player_id'] = player_id
            game_state['players'][player_id] = f"Player {player_id}"
            if game_state['turn'] is None:
                game_state['turn'] = player_id
            broadcast_message(f"Player {player_id} has joined the game.")

    player_id = session['player_id']

    if request.method == 'POST':
        if game_state['turn'] != player_id:
            return render_template('index.html', game=game_state, error="Not your turn!", player_id=player_id)

        action = request.form.get('action')
        if action == 'attack':
            damage = 10  # fixed damage for demo
            with lock:
                game_state['boss_hp'] -= damage
                if game_state['boss_hp'] < 0:
                    game_state['boss_hp'] = 0
                broadcast_message(f"Player {player_id} attacks boss for {damage} damage! Boss HP: {game_state['boss_hp']}")

                # Check boss defeated
                if game_state['boss_hp'] == 0:
                    broadcast_message("Boss defeated! Game over!")
                else:
                    # Change turn
                    players = list(game_state['players'].keys())
                    next_index = (players.index(player_id) + 1) % len(players)
                    game_state['turn'] = players[next_index]

        return redirect(url_for('index'))

    return render_template('index.html', game=game_state, player_id=player_id)

@app.route('/reset')
def reset():
    with lock:
        game_state['boss_hp'] = 100
        game_state['players'] = {}
        game_state['turn'] = None
        game_state['messages'] = []
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
