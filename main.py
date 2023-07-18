from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')

    if user_agent and 'Discordbot' in user_agent:
        # Discord scan bot detected, redirect to a specific URL
        return redirect('https://cdn.prod.www.spiegel.de/images/8375937e-26a0-4296-9823-c21e04577729_w1600_r1.7783985102420856_fpx53.97_fpy49.97.jpg')
    else:
        # Regular user (non-scan bot) detected, redirect to a different URL
        return redirect('https://discord.gg/RgyzBArR9M')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
