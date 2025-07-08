from flask import Blueprint, render_template, request, redirect, url_for
from .models import Bug
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    bugs = Bug.query.all()
    return render_template('index.html', bugs=bugs)

@main.route('/submit', methods=['POST'])
def submit_bug():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority')

    if title and description:
        new_bug = Bug(title=title, description=description, priority=priority, status='Open')
        db.session.add(new_bug)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:bug_id>')
def delete_bug(bug_id):
    bug = Bug.query.get_or_404(bug_id)
    db.session.delete(bug)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/resolve/<int:bug_id>')
def resolve_bug(bug_id):
    bug = Bug.query.get_or_404(bug_id)
    bug.status = 'Resolved'
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/edit/<int:bug_id>', methods=['GET', 'POST'])
def edit_bug(bug_id):
    bug = Bug.query.get_or_404(bug_id)

    if request.method == 'POST':
        bug.title = request.form.get('title')
        bug.description = request.form.get('description')
        bug.priority = request.form.get('priority')
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('edit.html', bug=bug)
