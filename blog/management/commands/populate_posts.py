from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args:Any, **options:Any):
        titles = [
    "The Future of AI",
    "Climate Change Solutions",
    "Remote Work Trends",
    "Quantum Computing Explained",
    "Renewable Energy Innovations",
    "Deep Learning Demystified",
    "Post-Pandemic Economic Outlook",
    "Blockchain in Finance",
    "Storytelling in Marketing",
    "Medical Technology Advances",
    "Space Exploration Challenges",
    "Psychology of Decision Making",
    "Evolution of Social Media",
    "The Art of Cooking",
    "Cultural Diversity in Society",
    "Sustainable Development Investments",
    "Globalization Impact",
]


        contents = [
    "The Future of AI: The future of AI holds great potential, with advances in natural language processing, autonomous vehicles, and AI-driven healthcare solutions. The integration of AI into industries promises to revolutionize processes, improve efficiency, and open new frontiers in creativity and problem-solving.",
    "Climate Change Solutions: Climate change solutions focus on reducing greenhouse gas emissions, transitioning to renewable energy sources, and implementing sustainable practices. Strategies such as carbon capture technology, reforestation, and the adoption of clean energy are essential to mitigating climate change.",
    "Remote Work Trends: Remote work trends have accelerated due to technological advancements and the global pandemic. Companies are adopting hybrid models, offering flexibility, and utilizing collaboration tools. Remote work has reshaped work-life balance and brought new challenges and opportunities in workforce management.",
    "Quantum Computing Explained: Quantum computing represents a breakthrough in computational power, leveraging quantum bits (qubits) to solve complex problems at speeds unimaginable by classical computers. It has the potential to revolutionize industries like cryptography, drug discovery, and materials science.",
    "Renewable Energy Innovations: Renewable energy innovations are driving the transition from fossil fuels to sustainable power sources. Advances in solar, wind, and hydroelectric technologies, along with battery storage solutions, are making clean energy more accessible and efficient than ever before.",
    "Deep Learning Demystified: Deep learning is a subset of machine learning that uses neural networks with many layers to analyze data. It has applications in image recognition, speech processing, and autonomous driving. Despite its complexity, deep learning is rapidly advancing and becoming more accessible to researchers and developers.",
    "Post-Pandemic Economic Outlook: The post-pandemic economic outlook is shaped by the recovery process, shifts in consumer behavior, and changes in the workforce. Governments are focusing on stimulus packages, digital transformation, and healthcare advancements to stabilize and grow economies around the world.",
    "Blockchain in Finance: Blockchain technology is transforming finance by providing a secure, decentralized way to process transactions. It reduces the need for intermediaries, enhances transparency, and enables the creation of digital currencies and smart contracts, reshaping financial services globally.",
    "Storytelling in Marketing: Storytelling in marketing is a powerful tool for connecting with audiences on an emotional level. By crafting compelling narratives around brands and products, companies can build stronger relationships with customers, drive engagement, and differentiate themselves in competitive markets.",
    "Medical Technology Advances: Medical technology advances are improving diagnosis, treatment, and patient care. Innovations like telemedicine, robotic surgery, and AI-powered diagnostic tools are enhancing healthcare delivery, making treatments more accurate and accessible to people around the world.",
    "Space Exploration Challenges: Space exploration faces challenges such as funding, technological limitations, and the harsh conditions of outer space. However, advancements in spacecraft technology, private sector involvement, and international collaborations are helping overcome these obstacles and pave the way for future space missions.",
    "Psychology of Decision Making: The psychology of decision making explores how people make choices and the cognitive biases that influence them. Understanding decision-making processes can improve outcomes in fields like business, healthcare, and education by optimizing strategies and minimizing errors.",
    "Evolution of Social Media: The evolution of social media has been marked by the rise of platforms like Facebook, Instagram, Twitter, and TikTok. Social media has become a dominant force in communication, marketing, and entertainment, with an increasing emphasis on user-generated content, privacy concerns, and algorithm-driven engagement.",
    "The Art of Cooking: The art of cooking is a blend of creativity, technique, and science. It involves combining ingredients, flavors, and textures to create dishes that are both delicious and visually appealing. Cooking is an ever-evolving skill that reflects cultural traditions, innovation, and personal expression.",
    "Cultural Diversity in Society: Cultural diversity in society enriches communities by bringing together people from different backgrounds, perspectives, and experiences. Embracing diversity fosters mutual respect, enhances creativity, and contributes to a more inclusive and dynamic social fabric.",
    "Sustainable Development Investments: Sustainable development investments focus on projects and technologies that promote economic growth while preserving environmental resources and improving social well-being. Green energy, eco-friendly construction, and ethical supply chains are key areas where sustainable investments are making a significant impact.",
    "Globalization Impact: The impact of globalization has led to greater interconnectivity between countries, cultures, and economies. While it has spurred economic growth, innovation, and access to new markets, it has also raised concerns about inequality, environmental degradation, and the loss of cultural identity."
]

        img_urls = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400"
]
        for title, content, img_url in zip(titles, contents, img_urls):
            Post.objects.create(title = title, content = content, img_url = img_url)
        
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
