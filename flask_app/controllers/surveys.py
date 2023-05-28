from flask_app import app
from flask import redirect, render_template,request, url_for
from ..models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/<int:id>')
def result(id):
    id_data = {
        'id': id
    }
    all_data = Survey.get_all_data(id_data)
    print(all_data)
    return render_template('result.html', all_data=all_data)


@app.route('/result/save', methods=['POST'])
def save_survey():
    print(request.form)
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "database": request.form.get('database'),
        "framework": request.form.get('framework'),
        "comment": request.form['comment']
    }
    if not data['database'] :
        data['database'] = None
    if not data['framework'] :
        data['framework'] = None
    
    if not Survey.validate_survey(data):
        return redirect('/')
    
    survey_id = Survey.save(data)
    print(survey_id)
    return redirect(url_for('result', id=survey_id))