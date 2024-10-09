use mysql;
CREATE TABLE JOBPORTALCOMPANYS (
    Company_Name VARCHAR(255) NOT NULL,
    Job_Released_Date VARCHAR(255) NOT NULL,
    Job_Position VARCHAR(255) NOT NULL,
    Package_CTC VARCHAR(255),
    Qualification VARCHAR(255) NOT NULL,
    Batch VARCHAR(255),
    Job_Summary TEXT NOT NULL,
    Eligibility_Criteria TEXT NOT NULL,    
    Experience VARCHAR(255) NOT NULL,
    Location VARCHAR(255) NOT NULL,
    Last_Date_to_Apply VARCHAR(255),
    Company_Name_Recruitment_2023 VARCHAR(255),
    About_Company TEXT NOT NULL,
    Job_Responsibilities TEXT NOT NULL,
    Preferred_Skills TEXT,
    Apply_Here_URL VARCHAR(255) NOT NULL
);
INSERT INTO JOBPORTALCOMPANYS (
    Company_Name,
    Job_Released_Date,
    Job_Position,
    Package_CTC,
    Qualification,
    Batch,
    Job_Summary,
    Eligibility_Criteria,
    Experience,
    Location,
    Last_Date_to_Apply,
    Company_Name_Recruitment_2023,
    About_Company,
    Job_Responsibilities,
    Preferred_Skills,
    Apply_Here_URL
) VALUES (
    'Cisco',
    '2023-04-13',
    'Consulting Engineer',
    '10 LPA (Expected)',
    'Bachelor’s Degree',
    '2018/ 2019/ 2020/ 2021/ 2022/ 2023',
    'Cisco is hiring for the position of Consulting Engineer in Bangalore, India. All the candidates of various disciplines eligible to apply for this job recruitment drive 2023. Interested Candidates can read more details and apply for this position.',
    'Ability to articulate and demonstrate business outcomes via technical delivery
Capability to design and stitch multiple architectures on-premises and in the cloud
Participate in larger technical forums such as Cisco Live or other industry forums.
Create whitepapers, knowledge articles, and patents to have a greater impact.
Experience/Knowledge/Awareness of R&S, Security, Wireless, and DC technologies in a multi-vendor environment.',
    '0 – 2 (Years)',
    'Bangalore , India',
     '-',
    'Cisco Recruitment Off-Campus Drive 2023',
    'Cisco was founded in 1984 by a small group of Stanford University computer scientists. Cisco engineers have been pioneers in the development of Internet Protocol (IP)-based networking technologies since the company’s inception. This tradition of innovation continues today, with more than 71,000 employees worldwide, with industry-leading products and solutions in the company’s core development areas of routing and switching, as well as in advanced technologies such as home networking, IP telephony, optical networking, security, storage area networking, and wireless technology.',
    'Successfully contribute to the areas of Customer Solution Design, Innovation, Engineering Engagement, Intellectual Capital, and Talent Development.
Mentor and develop other Consulting Engineers actively.
Leads the creation and sharing of intellectual property (content, training) for various audiences and customers, including digital intellectual property (e.g., scripts, software assets).
In support of partner concerns, provides technical expertise and guidance to resolve sophisticated customer problems.
Continual learning and improvement of technical skills in relevant technical domains and adjacent technologies.
Automation ideation avenues; lead and collaborate with a team of software programmers to implement automation ideas for delivery excellence and efficiency.
Consults with customers and Cisco partners to plan, design, install, configure, integrate, and/or optimise Cisco’s suite of products and services in order to accelerate business results.',
    'Mentor / develop other Engineers. 
Play the role of an individual contributor.
Mentorship impacts CX technical communities. ',
    'https://jobs.cisco.com/jobs/ProjectDetail/Consulting-Engineer/1387783?source=LinkedIn'
);
select * from jobportalcompanys;