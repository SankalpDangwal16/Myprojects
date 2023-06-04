# Assuming your dataset is stored in a variable called 'tennis_data'

# Load required libraries
library(ggplot2)
library(dplyr)
df <- read.csv("C:/Users/sanka/OneDrive/Desktop/atp_tennis.csv")
# Data exploration and summary statistics
summary(df)
str(df)
head(df)

df$Score <- as.character(df$Score)
df$Score <- gsub(" ", "", df$Score)
df$Score <- gsub("-", ":", df$Score)

# Count the frequency of each score
score_counts <- table(df$Score)

# Create a bar plot of score frequencies
ggplot(data = data.frame(Score = names(score_counts), Frequency = as.numeric(score_counts)),
       aes(x = Score, y = Frequency, fill = Score)) +
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("#4472C4", "#ED7D31", "#FFC000", "#5B9BD5", "#70AD47", "#9E480E", "#7F7F7F", "#C00000", "#00B050", "#964B00")) +
  labs(title = "Distribution of Match Scores", x = "Score", y = "Frequency") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))














# Data visualization
# Example: Bar chart of match outcomes
ggplot(tennis_data, aes(x = Winner)) +
  geom_bar() +
  labs(x = "Winner", y = "Count") +
  ggtitle("Match Outcomes")

# Data filtering and subsetting
# Example: Filter data for matches played on a specific surface
filtered_data <- subset(tennis_data, Surface == "Hard")

# Aggregation and grouping
# Example: Calculate average rank by player
average_rank <- tennis_data %>%
  group_by(Player_1) %>%
  summarise(Average_Rank = mean(Rank_1))

# Analyzing match outcomes
# Example: Calculate win percentage for each player
win_percentage <- tennis_data %>%
  group_by(Player_1) %>%
  summarise(Win_Percentage = sum(Winner == Player_1) / n())

# Hypothesis testing
# Example: Perform t-test to compare points between winners and losers
t_test <- t.test(tennis_data$Pts_1, tennis_data$Pts_2)

# Machine learning models
# Example: Build a logistic regression model to predict match winners
model_data <- tennis_data %>%
  select(Rank_1, Rank_2, Pts_1, Pts_2, Winner) %>%
  filter(!is.na(Rank_1), !is.na(Rank_2), !is.na(Pts_1), !is.na(Pts_2))

model <- glm(Winner ~ Rank_1 + Rank_2 + Pts_1 + Pts_2, data = model_data, family = binomial)

# Display model summary
summary(model)

ggplot(data = tennis_data, aes(x = Player_1, y = avg_rank)) +
  geom_point() +
  labs(title = "Average Rank of Players", x = "Player", y = "Average Rank") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1))

df$Score <- as.character(df$Score)
df$Score <- gsub(" ", "", df$Score)
df$Score <- gsub("-", ":", df$Score)
df$Score <- as.factor(df$Score)

# Create a histogram of match scores
ggplot(tennis_data, aes(x = Score)) +
  geom_bar(fill = "blue", alpha = 0.7) +
  labs(title = "Distribution of Match Scores", x = "Score", y = "Count") +
  theme_minimal()



df$Score <- as.character(df$Score)
df$Score <- gsub(" ", "", df$Score)
df$Score <- gsub("-", ":", df$Score)
df$Score <- as.factor(df$Score)

# Create a histogram of match scores
ggplot(tennis_data, aes(x = Score)) +
  geom_bar(fill = "blue", alpha = 0.7) +
  labs(title = "Distribution of Match Scores", x = "Score", y = "Count") +
  theme_minimal()

df$Score <- as.character(df$Score)
df$Score <- gsub(" ", "", df$Score)
df$Score <- gsub("-", ":", df$Score)
df$Score <- as.factor(df$Score)

# Create a bar plot of match scores
ggplot(tennis_data, aes(x = Score)) +
  geom_bar(fill = "blue", alpha = 0.7) +
  labs(title = "Distribution of Match Scores", x = "Score", y = "Count") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))


df$Score <- as.character(df$Score)
df$Score <- gsub(" ", "", df$Score)
df$Score <- gsub("-", ":", df$Score)

# Create a violin plot of match scores
ggplot(tennis_data, aes(x = Score, y = "", fill = Score)) +
  geom_violin(trim = FALSE) +
  scale_fill_manual(values = c("#4472C4", "#ED7D31", "#FFC000", "#5B9BD5", "#70AD47", "#9E480E", "#7F7F7F", "#C00000", "#00B050", "#964B00")) +
  labs(title = "Distribution of Match Scores", x = "Score", y = "") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))


score_counts <- table(df$Score)
observed <- as.numeric(score_counts)
expected <- rep(sum(score_counts) / length(score_counts), length(score_counts))

# Perform chi-squared test
result <- chisq.test(observed, p = expected)

# Print the test result
print(result)