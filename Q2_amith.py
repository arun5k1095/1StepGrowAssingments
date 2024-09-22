# Q2
# Task:
# Update the score in Math for Emma to 70.
# Add a subject "Python" for Noah and provide the score 95.
# Print the difference in the score in Science for Liam and Ava.
# Add your name to the dictionary and add your scores for all subjects.
# Nested dictionary containing students' scores in different subjects
students_scores = {
    "Emma": {"Math": 85, "Science": 90, "English": 78},
    "Liam": {"Math": 92, "Science": 88, "English": 95},
    "Olivia": {"Math": 70, "Science": 75, "English": 80},
    "Noah": {"Math": 88, "Science": 82, "English": 85},
    "Ava": {"Math": 95, "Science": 93, "English": 97}
}

# 1. Update the score in Math for Emma to 70
students_scores["Emma"]["Math"] = 70

# 2. Add a subject "Python" for Noah and provide the score 95
students_scores["Noah"]["Python"] = 95

# 3. Print the difference in score in Science for Liam and Ava
liam_science_score = students_scores["Liam"]["Science"]
ava_science_score = students_scores["Ava"]["Science"]
print("Difference in Science score between Liam and Ava:", liam_science_score - ava_science_score)

# 4. Add your name and scores
students_scores["YourName"] = {"Math": 85, "Science": 90, "English": 80}

# Print the updated dictionary
print("Updated students' scores:", students_scores)
# Explanation:
# We access and update the score for Emma using the key "Emma" and the sub-key "Math".
# We add a new subject "Python" with a score for Noah.
# We calculate and print the difference in the Science scores for Liam and Ava.
# Finally, we add a new entry for your name with your scores.


import java.util.HashMap;
import java.util.Map;

# public class StudentScoresUpdate {
#     public static void main(String[] args) {
#         // Creating a HashMap to store students' scores in specific subjects
#         Map<String, Map<String, Integer>> studentsScores = new HashMap<>();
#
#         // Populating the HashMap
#         studentsScores.put("Emma", new HashMap<>(Map.of("Math", 85, "Science", 90, "English", 78)));
#         studentsScores.put("Liam", new HashMap<>(Map.of("Math", 92, "Science", 88, "English", 95)));
#         studentsScores.put("Olivia", new HashMap<>(Map.of("Math", 70, "Science", 75, "English", 80)));
#         studentsScores.put("Noah", new HashMap<>(Map.of("Math", 88, "Science", 82, "English", 85)));
#         studentsScores.put("Ava", new HashMap<>(Map.of("Math", 95, "Science", 93, "English", 97)));
#
#         // 1. Update the score in Math for Emma to 70
#         studentsScores.get("Emma").put("Math", 70);
#
#         // 2. Add a subject "Python" for Noah with a score of 95
#         studentsScores.get("Noah").put("Python", 95);
#
#         // 3. Print the difference in Science score for Liam and Ava
#         int liamScience = studentsScores.get("Liam").get("Science");
#         int avaScience = studentsScores.get("Ava").get("Science");
#         System.out.println("Difference in Science score between Liam and Ava: " + (liamScience - avaScience));
#
#         // 4. Add your name and scores
#         studentsScores.put("YourName", new HashMap<>(Map.of("Math", 85, "Science", 90, "English", 80)));
#
#         // Print the updated dictionary
#         System.out.println("Updated students' scores: " + studentsScores);
#     }
# }
