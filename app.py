from flask import Flask, render_template
from dotenv import load_dotenv
import os
import stripe


app = Flask(__name__)

load_dotenv()

stripe_secret_key = os.getenv('STRIPE_SECRET_KEY')
stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/')
def create_payment():
    try:
        stripe_secret_key = stripe_secret_key
        checkout_session = stripe.checkout_Session.create(
            payment_method_types = ['cards'],
            line_items = [{
                'price': '{{PRICE_ID}}',
                'quantity': 1
            }],
            mode = 'payment',
            success_url = './success.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url = './cancel.html'
        )
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/success')
def payment_successful():
    return render_template('success.html')