# hack2024-copilot-for-kusto
The code repo for the Hackathon 2024 project Copilot for Kusto insights
Copilot for Kusto Insights
Unlock Insights with Ease, Simplify Data Analysis
Description
Project Description: Integrating Copilot with Kusto Explorer to Generate KQL Queries and Obtain Insights from Records Using Natural Language
1.	Problem Statement
A key part of resolving customer issues with various Microsoft products and services involves analyzing backend logs. Support staff and product teams usually need to run Kusto queries and manually identify trends and patterns in the extracted records to understand the root cause of the problem. Considerable time is spent on locating and crafting these queries, adjusting them for diverse customer scenarios, extracting relevant data, and creating visualizations like charts and tables for incident reports sent to the product team, as well as preparing Excel sheets or similar files with shareable data for customers. New engineers also need to invest time in learning KQL syntax. Moreover, many customers utilise KQL queries in services such as Log Analytics, often opening support cases where they seek assistance in finding the right queries to obtain correct results.
Copilot for Kusto Insights is a tool designed to simplify the process of extracting insights on customers’ usage of different services from backend logs. By integrating Copilot with Kusto, engineers and customers can leverage natural language processing to compose KQL queries, identify patterns in the records retrieved, and derive insights, all through prompts in simple English. The tool aims to enhance the efficiency and accuracy of data analysis, making it accessible to Microsoft engineers and customers with varying levels of expertise in KQL, thus reducing the time taken to troubleshoot intricate issues.
2.	Key Features of the Solution
•	Natural Language Interface for Users: Engineers can write Kusto queries using simple English language, eliminating the need for deep knowledge of KQL syntax. This feature leverages natural language processing to translate user commands into accurate Kusto queries.

•	Maintain the Context of the Conversation: The Copilot will keep distinct contexts for each tab, and the session will terminate when the tab is closed.

•	Filtering out Irrelevant Records: The tool shall also be able to filter out irrelevant results based on prompts input in natural language, ensuring that only the most pertinent data is presented. For example, if a user asks for records corresponding to a particular operation or calls made between specific timestamps, the tool will focus on those criteria and exclude unrelated data.

•	Inherently Compliant Queries: Copilot for Kusto aims to comply with different compliance guidelines set for different teams, for example, the EUDB compliance guidelines and PII/EUI/EUPII/etc. which will ensure the queries are processed in respective geographies and help ensure that output also doesn’t contain any PII.
Additionally, visibility will be limited to the connections that are added, ensuring the user retains access solely to the records and tables they are authorized to view.

•	Detecting Patterns in Logs – Intelligent Overview: When troubleshooting customer problems, users often need to identify patterns in the retrieved records, such as specific error codes, recurring operations, or types of APIs used. The Copilot will facilitate this process by recommending patterns it has detected in the output of the executed query.

•	Optimized and Cost-Effective Queries: While users learn to make their queries specific, less resource-intensive and precise, this Copilot will help them speed up the journey by suggesting an optimized version of their query which will result in faster results and less resource consumption on Kusto clusters.

•	Prompt Suggestions to Start the Conversation: Copilot for Kusto Insights shall be able to propose initial prompts to initiate troubleshooting, such as "Fetch logs for me," and then progressively request details like resource IDs, timestamps, etc. (the typical Copilot interaction).

•	Proposing Follow-Up Questions: When analyzing a large or unfamiliar dataset to pinpoint an issue or discover a pattern, Copilot can help you explore the data from various perspectives. Some of these suggestions might be more beneficial than others for comprehending and presenting the data. For example, after displaying records as a bar chart, asking “Would a line chart be preferable?” can be advantageous.
3. Solution Using Azure Architecture
The approach utilizes Azure OpenAI’s natural language processing (NLP) to handle English language prompts and leverages its code-generation capabilities for creating KQL queries. The Assistants API facilitates the Copilot experience, ensuring distinct message contexts are preserved for each tab in the Data Explorer or Kusto Explorer interface using threads.
•	Azure Data Explorer: Acts as the interface for Copilot conversations. Data is retrieved using standard Kusto queries. The Copilot icon is present in every tab, enabling the user to access it whenever needed.
•	Azure OpenAI: Used for its Natural language processing (NLP) to handle English language prompts and leverages its code-generation capabilities for creating and fine-tuning KQL queries. 
4.	User Interface
The UI would be like that of the DfM Copilot, with a Copilot icon added to every tab on the Data Explorer. 

 
Upon clicking the Copilot button, the Copilot window will fly out from the right, with suggestions for prompts to start the conversation, like so:
 
The Copilot would maintain separate context for each tab, and the session would be closed when the tab is closed.
5. Data Used
The Copilot will only have access to the data retrieved through specific queries executed within a particular tab in the Data Explorer. Its visibility will be restricted to the added connections, guaranteeing that users can only use the records and tables which they are authorized to.
6.	Phased Approach to Developing the Solution
The solution can be developed in two major phases, to prioritize essential features and targeted users:
Phase 1: Rollout to Microsoft’s Internal Engineering and Support Teams
This phase would look at integrating Copilot with Azure Data Explorer and the desktop app Kusto Explorer for internal employees who use Kusto queries, to provide the essential features to users – generating KQL queries from natural language prompts, proposing follow up questions and providing basic insights on the records fetched. This should be done while maintaining the context separately for each tab, and with strict adherence to guidelines related to PII and other privacy and legal requirements.
Feedback has to be sought from the internal users regularly so that there is a continuous process of refining the performance of the tool in the process of optimizing queries to fit customer use cases and suggesting cost-effective queries. 
Phase 2: Expanding to External Customers
The second phase focuses on incorporating Copilot with customer-oriented services such as Azure Log Analytics and Azure Application Insights. This aims to expand the functionalities already accessible to Microsoft's internal users to their external clientele, while strictly adhering to PII and privacy regulations. The ongoing feedback process will continue to provide insights for enhancing the user experience.
7. Impact of the Solution
The entire solution provides several tangible benefits:
•	Faster Resolution of Support Cases: Automating query generation, trend analysis in backend logs, and the creation of visualizations or files reduces the manual effort needed from support engineers, significantly cutting down troubleshooting and incident reporting time. This leads to quicker resolution of support cases, saving time that could be utilized in upskilling.
•	Quicker Root Cause Analyses for Product Teams: Product teams can utilize trend analysis features and extract insights from backend logs in critical situations like outages, enabling quicker identification of the underlying issue, ultimately reducing Customer Pain Time.
•	Reduced Advisory Support Cases: Several advisory support cases stem from customers' insufficient knowledge of KQL when they attempt to use Kusto queries on services such as Azure Log Analytics for better usage insights. This Copilot can effortlessly guide them through the process, offering query suggestions as needed.
•	Reduced Resource Usage for Queries: As users become adept at crafting more specific and efficient queries over time, this Copilot will expedite the process by recommending optimized query versions. This leads to faster results and decreased resource consumption on Kusto clusters.
8. Features of Azure OpenAI Used in this Solution
•	NLP Models: Azure OpenAI's gpt-4o, a robust language model, evaluates user input prompts and produces insightful responses.
•	Code Generation: Composes KQL queries based on the inputs provided in natural language.
•	Assistants API: The Assistants API facilitates the Copilot experience in two ways:
o	Conversational AI Functions: Generates a conversational, chatbot-style interaction by offering suggestions for initial prompts and progressively enhancing them as additional records are accessed and further insights are discovered.
o	Usage of Threads: Ensures distinct message contexts are preserved for each tab in the Data Explorer or Kusto Explorer interface.
9. Business Value of Azure OpenAI to Microsoft Customers
•	Operational Efficiency: Automates tasks like writing queries, finding patterns in data and exporting data into files, reducing manual effort and accelerating resolution of support cases and incidents.
•	Enhanced Customer Experience: By reducing manual efforts and time spent by engineers on backend logs, customer pain time is significantly decreased, allowing for smooth customer experience.
•	Expanding the Solution to Customers: The solution can eventually be made available to customers who use KQL to fetch usage data on different Azure services.
10. Rapid, Broad, or Deep Use of Azure Resulting from this Solution
•	Rapid Use: Quick deployment of the solution can enable engineers to adopt and adjust to the Copilot, and provide constructive feedback over a few months, helping resolve customers’ issues quicker and refining the Copilot’s capabilities at the same time.
•	Broad Use: This Copilot can be adopted by a significant number of Microsoft’s internal teams, and eventually be rolled out to customers.
•	Deep Use: This solution relies heavily on the usage of Azure OpenAI’s Assistants API. Multiple threads used for multiple sets of queries for different user scenarios will facilitate greater usage of Azure OpenAI, and a deeper adoption of the Assistants API.
This project demonstrates the power of Azure in solving real-world problems, facilitating quicker resolution of customer issues, portraying the customer-obsession which is one of the core values of Microsoft.
