from textblob import TextBlob
import matplotlib.pyplot as plt

# Read survey responses
with open("survey_data.txt", "r") as file:
    responses = file.readlines()

positive = 0
negative = 0
neutral = 0

for response in responses:
    analysis = TextBlob(response)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        positive += 1
    elif polarity < 0:
        negative += 1
    else:
        neutral += 1

print("Survey Sentiment Analysis")
print("Positive:", positive)
print("Negative:", negative)
print("Neutral:", neutral)

labels = ['Positive', 'Negative', 'Neutral']
values = [positive, negative, neutral]

plt.bar(labels, values)
plt.title("Survey Feedback Analysis")
plt.xlabel("Feedback Type")
plt.ylabel("Number of Responses")

plt.show()