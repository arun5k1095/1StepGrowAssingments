# Dictionary containing students' scores
students_scores = {
    "Emma": [85, 90, 78],
    "Liam": [92, 88, 95],
    "Olivia": [70, 75, 80],
    "Noah": [88, 82, 85],
    "Ava": [95, 93, 97]
}

# 1. Calculate the average score of Olivia
olivia_scores = students_scores["Olivia"]
olivia_average = sum(olivia_scores) / len(olivia_scores)
print("Average score of Olivia:", olivia_average)

# 2. Calculate the average score of Liam
liam_scores = students_scores["Liam"]
liam_average = sum(liam_scores) / len(liam_scores)

# Calculate the difference in average scores between Liam and Olivia
difference = liam_average - olivia_average
print("Difference in average score of Liam and Olivia:", difference)


# public class StudentScores {
#     public static void main(String[] args) {
#         // Creating a HashMap to store students' scores
#         Map<String, int[]> studentsScores = new HashMap<>();
#         studentsScores.put("Emma", new int[]{85, 90, 78});
#         studentsScores.put("Liam", new int[]{92, 88, 95});
#         studentsScores.put("Olivia", new int[]{70, 75, 80});
#         studentsScores.put("Noah", new int[]{88, 82, 85});
#         studentsScores.put("Ava", new int[]{95, 93, 97});
#
#         // Calculate the average score of Olivia
#         int[] oliviaScores = studentsScores.get("Olivia");
#         double oliviaAverage = calculateAverage(oliviaScores);
#
#         // Calculate the average score of Liam
#         int[] liamScores = studentsScores.get("Liam");
#         double liamAverage = calculateAverage(liamScores);
#
#         // Print the results
#         System.out.println("Average score of Olivia: " + oliviaAverage);
#         System.out.println("Difference in average score of Liam and Olivia: " + (liamAverage - oliviaAverage));
#     }
#
#     // Helper method to calculate the average of an array of integers
#     public static double calculateAverage(int[] scores) {
#         int sum = 0;
#         for (int score : scores) {
#             sum += score;
#         }
#         return sum / (double) scores.length;
#     }
# }