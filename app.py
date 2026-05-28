def explain_topic(topic):
    return f"""
Topic: {topic}

Simple Explanation:
This section explains {topic} in a clear and easy way for Army board study.

Study Tips:
1. Know the definition.
2. Know why it matters.
3. Know how Soldiers use it.
4. Be ready to explain it in your own words.

Quiz:
1. What is {topic}?
2. Why is {topic} important?
3. Who is responsible for knowing {topic}?
4. How does {topic} affect Soldiers?
5. How would you explain {topic} to a new Soldier?
"""

print("AI Army Board Study Assistant")
topic = input("Enter a topic you want to study: ")
print(explain_topic(topic))
