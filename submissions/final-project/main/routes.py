from main import app, db
from flask import render_template, request, redirect
from main.models import Website

@app.route('/')
@app.route('/home')
def home():
    delete_mode = request.args.get('deletemode', default=False)
    websites = Website.query.all()
    # output = []
    # for website in websites:
    #     website_data = {
    #         'id': website.id,
    #         'website': website.website,
    #         'email': website.email,
    #         'password': website.password,
    #         'description': website.description
    #     }
    #     output.append(website_data)
    return render_template('home.html',websites=websites, delete_mode=delete_mode)

@app.route('/add_website', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('edit-website.html', edit=False)
    if request.method == 'POST':
        website = request.form['website']
        email = request.form['email']
        password = request.form['password']
        description = request.form['description']
        new_website = Website(website=website, email=email, password=password, description=description)
        db.session.add(new_website)
        db.session.commit()
        return redirect('/')
    
@app.route('/delete_website', methods=['POST'])
def delete():
    website_id = request.form['website_id']
    website = Website.query.get(website_id)
    db.session.delete(website)
    db.session.commit()
    return redirect('/?deletemode=True')

@app.route('/edit_website/<website_id>', methods=['GET', 'POST'])
def edit(website_id):
    website = Website.query.get(website_id)
    if request.method == 'GET':
        return render_template('edit-website.html', edit=True, website=website)
    if request.method == 'POST':
        website.website = request.form['website']
        website.email = request.form['email']
        website.password = request.form['password']
        website.description = request.form['description']
        db.session.commit()
        return redirect('/')