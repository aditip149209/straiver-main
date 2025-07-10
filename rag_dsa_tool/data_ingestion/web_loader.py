from langchain_community.document_loaders import WebBaseLoader

urls = ["https://roadmap.sh/typescript", "https://roadmap.sh/git-github", "https://roadmap.sh/javascript", "https://roadmap.sh/sql",
        "https://roadmap.sh/cpp", "https://roadmap.sh/python", "https://roadmap.sh/redis", "https://roadmap.sh/system-design",
        "https://roadmap.sh/software-design-architecture", "https://roadmap.sh/prompt-engineering", "https://roadmap.sh/ai-agents",
        "https://roadmap.sh/backend", "https://roadmap.sh/docker", "https://roadmap.sh/ai-red-teaming", "https://roadmap.sh/cyber-security",
        "https://roadmap.sh/devops", "https://roadmap.sh/software-design-architecture", "https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/",
        "https://leetcode.com/studyplan/top-interview-150/"]
loader = WebBaseLoader(urls)
website_docs = loader.load()

