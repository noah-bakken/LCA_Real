from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'noahbakken477@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('GMAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Function to get upcoming events
def upcoming_events():
    return [
        {
            'title': 'Insights & Innovation',
            'description': "Come HCN, 812 Consulting, and LCA for a panel with Big 3 Interns!",
            'date': '2024-10-17',
            'location': 'Myles Brand 107 @7:30pm',
            'image': 'images/events/insights_innovation.jpg'
        }
    ]

# Function to get all other events
def all_events():
    return [
        {'title': 'Interview Workshop with Career Services',
            'description': "Come join us with Luddy Career Services on how to successfully complete interviews.",
            'date': '2024-10-15',
            'location': 'Myles Brand',
            'image': 'images/events/interview_workshop.png'},
        {
            'title': 'Deloitte Career Connect',
            'description': "Deloitte Consultants came in to help students learn about Deloitte's culture and navigate internships and full-time roles.",
            'date': '2024-11-10',
            'image': 'images/events/deloitte_2024.webp'
        },
        {
            'title': 'Crowe Recruitment Event',
            'description': 'Recruiters from Crowe spoke to LCA members about careers at Crowe and how to navigate the job market.',
            'date': '2024-12-05',
            'image': 'images/events/crowe_2024.webp'
        },
        {
            'title': 'EY Networking Event',
            'description': 'EY consultants shared insights about their consulting practice.',
            'date': '2024-12-15',
            'image': 'images/events/ey_2024.webp'
        },
        {
            'title': 'Grant Thornton Insights',
            'description': 'Grant Thornton professionals talked about services and opportunities in their firm.',
            'date': '2024-12-20',
            'image': 'images/events/grant_thornton_2024.webp'
        },
    ]

@app.route('/')
def home():
    events = upcoming_events()  # Get upcoming events dynamically
    workshops = [
        {
            'title': 'ServiceNow',
            'description': 'LCA tech consultants participated in a ServiceNow boot camp run by Deloitte consultants.'
        },
        {
            'title': 'Case Competition',
            'description': 'LCA members were in the top groups for a cross-organizational market penetration case competition.'
        },
        {
            'title': 'Placeholder Workshop',
            'description': 'This workshop will cover important consulting skills.'
        },
        {
            'title': 'Placeholder Workshop',
            'description': 'Another upcoming consulting workshop.'
        },
    ]
    return render_template('index.html', events=events, workshops=workshops)

@app.route('/events')
def events_page():
    upcoming = upcoming_events()  # Get upcoming events
    events = all_events()  # Get all other events
    return render_template('events.html', upcoming_events=upcoming, events=events)

# Member Routes
@app.route('/exec-members')
def exec_members():
    return render_template('exec_members.html')

@app.route('/tech-members')
def tech_members():
    return render_template('tech_members.html')

@app.route('/marketing-members')
def marketing_members():
    return render_template('marketing_members.html')

@app.route('/external-relations-members')
def external_relations_members():
    return render_template('external_relations.html')

@app.route('/finance-members')
def finance_members():
    return render_template('finance_members.html')

@app.route('/digital-solutions-members')
def digital_solutions_members():
    return render_template('digital_solutions_members.html')


@app.route('/tech-consulting-members')
def tech_consulting_members():
    return render_template('tech_consulting_members.html')


@app.route('/intern-members')
def intern_members():
    return render_template('intern_members.html')



@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        msg = Message(subject=f"Inquiry from {name}: {subject}",
                      sender='noahbakken477@gmail.com',
                      recipients=['noahbakken477@gmail.com'])

        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            mail.send(msg)
            flash('Your inquiry has been successfully sent!', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/workshops')
def workshops_page():
    workshops = [
        {
            'title': 'ServiceNow',
            'description': 'LCA tech consultants participated in a ServiceNow boot camp run by Deloitte consultants.',
            'image': 'images/events/service_now_workshop.jpg'
        },
        {
            'title': 'Case Competition',
            'description': 'LCA members were in the top groups for a cross-organizational market penetration case competition.',
            'image': 'images/events/case_comp.jpg'
        },
    ]
    return render_template('workshops.html', workshops=workshops)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')

    msg = Message('New Subscription',
                  sender='noahbakken477@gmail.com',
                  recipients=['noahbakken477@gmail.com'])

    msg.body = f'You have a new subscriber: {email}'

    try:
        mail.send(msg)
        flash('Subscription successful! A confirmation email has been sent.', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')

    return redirect(url_for('home'))

@app.context_processor
def inject_now():
    return {'current_year': datetime.utcnow().year}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
