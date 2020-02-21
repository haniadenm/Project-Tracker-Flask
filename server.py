"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route('/search')
def search():

    """Search for student by github username"""

    return render_template("student_search.html")


@app.route('/student')
def get_student():
    """Show information about a student."""

    github_value = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github_value)

    return render_template("student_info.html", first_name=first,
                           last_name=last,
                           github_user=github)


if __name__ == '__main__':
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
