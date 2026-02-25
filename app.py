from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_timetable(study_hours):
    timetable = "\n📅 Suggested Daily Timetable:\n"

    if study_hours >= 6:
        timetable += """
6:00 AM  - Wake Up & Exercise
7:00 AM  - Study Session 1
9:00 AM  - Break
10:00 AM - Study Session 2
1:00 PM  - Lunch
2:00 PM  - Practice / Revision
5:00 PM  - Short Break
6:00 PM  - Skill Development
9:30 PM  - Light Revision
10:30 PM - Sleep
"""
    else:
        timetable += """
7:00 AM  - Wake Up
8:00 AM  - Study 2 Hours
11:00 AM - Break
4:00 PM  - Study 2 Hours
8:00 PM  - Revision
10:30 PM - Sleep
"""
    return timetable


def get_motivation():
    quotes = [
        "🔥 Success is built by daily discipline.",
        "🚀 Small progress every day leads to big success.",
        "💪 Your habits decide your future.",
        "🌟 Stay consistent. Results will follow.",
        "🎯 Focus on goals, not distractions."
    ]
    return random.choice(quotes)


def analyze_future(name, interest, strength, study_hours, mobile_hours, habit, question):

    study_hours = int(study_hours)
    mobile_hours = int(mobile_hours)

    response = f"\nHello {name} 👋\n\n"

    study_score = min(study_hours * 10, 60)
    mobile_score = max(20 - (mobile_hours * 5), 0)
    habit_score = 20 if "discipline" in habit.lower() else 10

    total_score = study_score + mobile_score + habit_score

    if study_hours >= 6:
        response += "✅ Good study hours.\n"
    else:
        response += "⚠ Increase study time to minimum 6 hours daily.\n"

    if mobile_hours >= 8:
        response += "🚨 High Mobile Usage! Reduce screen time immediately.\n"
    elif mobile_hours >= 5:
        response += "⚠ Mobile usage is high. Try reducing it.\n"
    else:
        response += "✅ Mobile usage under control.\n"

    response += f"\n🎯 Career Suggestion for {interest}:\n"

    interest_lower = interest.lower()

    if "engineering" in interest_lower:
        response += "• Choose B.E / B.Tech\n• Improve Maths & Coding\n"
    elif "medical" in interest_lower:
        response += "• Prepare for NEET\n• Focus on Biology\n"
    elif "it" in interest_lower or "computer" in interest_lower:
        response += "• Learn Python / Java\n• Build Projects\n"
    else:
        response += "• Research deeply about your interest field\n"

    response += f"\n💪 Strength: {strength}\n"
    response += f"🧠 Habit: {habit}\n"

    if question:
        q = question.lower()
        if "salary" in q:
            response += "\nHigh skills = High salary.\n"
        elif "abroad" in q:
            response += "\nPrepare IELTS & maintain good CGPA.\n"
        else:
            response += "\nStay consistent daily.\n"

    response += generate_timetable(study_hours)

    response += "\n\n✨ Motivation of the Day:\n"
    response += get_motivation()

    response += f"\n\n📊 Career Readiness Score: {total_score}%"

    return response


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""

    if request.method == "POST":
        name = request.form.get("name")
        interest = request.form.get("interest")
        strength = request.form.get("strength")
        study_hours = request.form.get("study_hours")
        mobile_hours = request.form.get("mobile_hours")
        habit = request.form.get("habit")
        question = request.form.get("question")

        if name and interest and strength and study_hours and mobile_hours and habit:
            answer = analyze_future(name, interest, strength, study_hours, mobile_hours, habit, question)
        else:
            answer = "⚠ Please fill all fields properly."

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)