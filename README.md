### FYP Final Year Description
## Introduction
We are proud to present our Final Year Project (FYP), NAaaS (News Analytics as a Service). NAaaS revolutionizes the way news is accessed and analyzed, offering a comprehensive solution for obtaining relevant news information within specified timeframes. Gone are the days of manual searches and sifting through numerous articles. With NAaaS, we have streamlined the process through advanced automation techniques and cutting-edge technologies.

## Problem Statement
Traditionally, when seeking news on specific topics over extended periods, users were left with two options. They could either rely on third-party sources, hoping someone had already done the legwork, or manually scour news archives, painstakingly examining each article to find the desired information. Imagine the time and effort required for searching through years of news manually—it was simply impractical.

## Solution: NAaaS Features
NAaaS tackles this challenge head-on by implementing automated scraping techniques to gather news from various online resources. Our system extracts key details such as time, location, and category from each article, empowering users to find their desired news easily. The categories are dynamically assigned based on the content of the news articles, adapting to the ever-evolving news landscape. By visualizing the news on a map, NAaaS takes on the appearance of a Geographic Information System (GIS), enhancing the user experience.

## Focus Time and Locations
Understanding the importance of context, NAaaS provides crucial information about the focus time and locations for each news article. Consider an event that took place in State A a week ago, with subsequent hearings scheduled in State B. A news headline may read, "State A: Court Orders $100 Fine in XYZ Case." Merely reading the headline would lead one to believe that the news pertains to State A and is current. However, upon reading the entire paragraph, it becomes apparent that the news refers to an event that occurred a week ago in State A, with the court hearing taking place in State B. By providing these details, NAaaS ensures accurate categorization and interpretation of news articles.

## Use Case
NAaaS caters to individuals interested in staying informed about local events and activities. With our user-friendly interface, users can effortlessly explore what is happening in their vicinity. By selecting a location, a polygon is drawn on the map, displaying relevant news articles within that area. The side section of the interface provides a comprehensive list of articles, categorized and color-coded for ease of understanding.

## Challenge: Real-Time Updates and Big Data Processing
News updates occur rapidly, requiring our map to be dynamic and constantly updated. As new articles are published, NAaaS seamlessly integrates them into the system. Given the immense volume of data to process, we employ distributed processing techniques using Spark and Kafka, industry-leading big data tools. To ensure scalability and efficiency, we utilize Docker images, providing a lightweight and standardized solution that meets industrial standards.

For a detailed description of our Final Year Project, please contact me at m.butt_@outlook.com
