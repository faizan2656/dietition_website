import urllib.parse
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

PLANS = [
    {
        "num": "01",
        "title": "Fat Loss",
        "desc": (
            "Personalized nutrition plans designed to support sustainable fat"
            " loss while helping you enjoy a balanced diet."
        ),
    },
    {
        "num": "02",
        "title": "Fat Loss + Muscle Gain",
        "desc": (
            "A balanced nutrition approach focused on improving body"
            " composition and supporting muscle growth."
        ),
    },
    {
        "num": "03",
        "title": "PCOS & PMS Support",
        "desc": (
            "Personalized nutrition guidance to support hormonal health and"
            " manage symptoms effectively."
        ),
    },
    {
        "num": "04",
        "title": "Diabetes Nutrition",
        "desc": (
            "Customized plans focused on balanced meals and better blood glucose"
            " management."
        ),
    },
    {
        "num": "05",
        "title": "Pregnancy Nutrition",
        "desc": (
            "Personalized nutrition guidance designed to support changing"
            " nutritional needs throughout pregnancy."
        ),
    },
    {
        "num": "06",
        "title": "Postpartum Nutrition",
        "desc": (
            "Nutritional support tailored to postpartum recovery and building"
            " healthy family eating habits."
        ),
    },
    {
        "num": "07",
        "title": "Weight Maintenance",
        "desc": (
            "Focused on maintaining a healthy weight while enjoying a flexible"
            " and sustainable lifestyle."
        ),
    },
    {
        "num": "08",
        "title": "Disease-Related Nutrition",
        "desc": (
            "Personalized therapeutic nutrition support tailored to specific"
            " health conditions."
        ),
    },
]

FAQS = [
    {
        "q": "Is my nutrition plan personalized?",
        "a": (
            "Yes. Every plan is customized according to your goals, lifestyle,"
            " routine, food preferences, and individual nutritional needs."
        ),
    },
    {
        "q": "What coaching durations do you offer?",
        "a": (
            "I offer 30-day, 60-day, and 90-day personalized coaching plans,"
            " depending on your goals and requirements."
        ),
    },
    {
        "q": "Will I get multiple meal options?",
        "a": (
            "Yes. Your plan includes multiple meal options, along with"
            " calorie-counted recipes and practical food choices to keep your"
            " diet enjoyable and flexible."
        ),
    },
    {
        "q": "Can I swap meals or ingredients?",
        "a": (
            "Yes. Flexible food swaps are provided so you can adjust your meals"
            " according to your preferences, availability, and routine."
        ),
    },
    {
        "q": "Do you provide nutrition plans for health conditions?",
        "a": (
            "Yes. I offer personalized disease-related and therapeutic nutrition"
            " plans, along with specific plans for areas such as PCOS/PMS and"
            " diabetes, based on individual assessment."
        ),
    },
    {
        "q": "How do I apply for coaching?",
        "a": (
            "Start by completing the online assessment form. Once your"
            " information is reviewed, you will be guided through the next"
            " steps and suitable coaching option."
        ),
    },
    {
        "q": "How is the coaching fee determined?",
        "a": (
            "Since every coaching plan is personalized, pricing may vary"
            " depending on the selected program and individual requirements."
            " The exact fee will be shared after assessment."
        ),
    },
]


@app.route("/")
def home():
  return render_template("index.html", plans=PLANS, faqs=FAQS)


@app.route("/submit-assessment", methods=["POST"])
def submit_assessment():
  name = request.form.get("clientName", "N/A")
  phone = request.form.get("clientPhone", "N/A")
  age = request.form.get("clientAge", "N/A")
  gender = request.form.get("clientGender", "N/A")
  feet = request.form.get("clientFeet", "0")
  inches = request.form.get("clientInches", "0")
  weight = request.form.get("clientWeight", "N/A")
  goal = request.form.get("clientGoal", "N/A")
  medical = request.form.get("clientMedical", "None")

  # Standardized WhatsApp International Format
  whatsapp_number = "923115244757"

  msg = (
      "🌿 *New Client Assessment Submission*\n\n"
      f"👤 *Name:* {name}\n"
      f"📞 *Phone:* {phone}\n"
      f"🎂 *Age:* {age} years\n"
      f"🚻 *Gender:* {gender}\n"
      f"📏 *Height:* {feet} ft {inches} in\n"
      f"⚖️ *Weight:* {weight} kg\n"
      f"🎯 *Selected Goal:* {goal}\n"
      f"📋 *Medical History / Notes:* {medical}\n\n"
      "_Submitted via DN. Faryal Tahir Portal_"
  )

  encoded_msg = urllib.parse.quote(msg)
  target_url = (
      f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_msg}"
  )

  return redirect(target_url)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)

# Ye line Vercel ke liye lazmi add karein:
app = app
