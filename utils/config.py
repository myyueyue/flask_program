from flask import Flask
import os
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
