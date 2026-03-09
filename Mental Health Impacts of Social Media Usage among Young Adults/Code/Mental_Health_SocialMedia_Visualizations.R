# ============================================
# Project: Mental Health Impacts of Social Media Usage
# Visualizations Script
# Author: Arulsree Mozhi & Thangaraj Santhakumar
# Date: 05/24/2024
# ============================================

# --- Load Libraries ---
suppressPackageStartupMessages({
  library(ggplot2)
  library(dplyr)
  library(tidyr)
  library(readxl)
  library(forcats)
  library(scales)
  library(cowplot)  # for combining plots
})

# --- 1. Pew Research Center Social Media Usage by Age ---
Pew_cleaned_data <- data.frame(
  social_media = c("Facebook","Instagram","LinkedIn","Twitter","Pinterest",
                   "Snapchat","YouTube","WhatsApp","Reddit","TikTok","BeReal"),
  age_18_29 = c(67,78,32,42,45,65,93,32,44,62,12),
  age_30_49 = c(75,59,40,27,40,30,92,38,31,39,3),
  age_50_64 = c(69,35,31,17,33,13,83,29,11,24,1),
  age_65_plus = c(58,15,12,6,21,4,60,16,3,10,0)
)

# Reshape data
Pew_long <- Pew_cleaned_data %>%
  pivot_longer(cols = starts_with("age_"), 
               names_to = "age_group", values_to = "percentage") %>%
  mutate(age_group = gsub("age_|_", "-", age_group))

# Plot 1: Grouped Bar Chart
plot1 <- ggplot(Pew_long, aes(x = social_media, y = percentage, fill = age_group)) +
  geom_bar(stat="identity", position="dodge") +
  theme_minimal() +
  labs(title="Social Media Usage by Age Group",
       x="Platform", y="Percentage of Users", fill="Age Group") +
  theme(axis.text.x = element_text(angle=45, hjust=1))

# --- 2. Mental Health Survey by Demographics ---
NI_cleaned_data <- data.frame(
  classification = c(rep("Sex",3), rep("Age",3), rep("Race/Ethnicity",6)),
  sub_classification = c("Overall","Female","Male","18-25","26-49","50+",
                         "Hispanic or Latino","White","Black or African American",
                         "NH/OPI","AI/AN","Asian"),
  percent = c(22.8,27.2,18.1,33.7,28.1,15,20.7,23.9,21.4,18.1,26.6,16.4)
)

# Reorder levels
NI_cleaned_data$sub_classification <- fct_relevel(
  NI_cleaned_data$sub_classification,
  "Male","Female","Overall","18-25","26-49","50+",
  "Hispanic or Latino","White","Black or African American",
  "NH/OPI","AI/AN","Asian"
)

# Plot 2: Stacked Bar Chart
plot2 <- ggplot(NI_cleaned_data, aes(x=sub_classification, y=percent, fill=classification)) +
  geom_bar(stat="identity", position="dodge") +
  theme_minimal() +
  labs(title="Mental Health Prevalence by Demographics",
       x="Sub-Classification", y="Percent (%)", fill="Classification") +
  theme(axis.text.x = element_text(angle=45, hjust=1)) +
  scale_fill_manual(values=c("Sex"="lightgreen","Age"="pink","Race/Ethnicity"="lightblue"))

# --- 3. Twitter Reply Counts Over Time ---
TW_cleaned_data <- data.frame(
  process_dt = seq(as.Date("2021-01-01"), as.Date("2021-01-10"), by="days"),
  reply_cnt = c(5,8,12,7,10,6,15,9,11,8),
  cluster = factor(c(1,2,3,1,2,3,1,2,3,1))
)

# Plot 3: Stacked Area Chart
plot3 <- ggplot(TW_cleaned_data, aes(x=process_dt, y=reply_cnt, fill=cluster)) +
  geom_area(position="stack") +
  scale_fill_manual(values=c("purple","turquoise","red")) +
  theme_minimal() +
  labs(title="Stacked Reply Counts Over Time by Cluster",
       x="Date", y="Reply Count", fill="Cluster") +
  scale_x_date(labels = date_format("%b-%d")) +
  theme(axis.text.x = element_text(angle=45, hjust=1))

# --- 4. Social Media Engagement Scatter by Age ---
plot4 <- ggplot(Pew_long, aes(x=age_group, y=percentage, color=social_media)) +
  geom_point(size=3) +
  theme_minimal() +
  labs(title="Social Media Engagement by Age Group",
       x="Age Group", y="Percentage of Users", color="Platform")

# --- Combine All Plots into a Grid ---
combined_plot <- plot_grid(plot1, plot2, plot3, plot4, ncol=2, labels = c("A","B","C","D"))
print(combined_plot)