# AI Career Roadmap Generator

A next-generation AI-powered career development platform that acts as a personal mentor, tutor, and interview coach.

## 🎯 Overview

This platform creates personalized, adaptive, and interview-ready learning roadmaps for users aiming for tech roles (Software Developer, AI Engineer, Data Scientist, Full Stack, etc.).

**This is NOT a static roadmap app.**  
It behaves like an **AI mentor + career coach + interviewer**.

## ✨ Key Features

- 🤖 **4 Specialized AI Agents** working together
  - Planner Agent: Designs your learning path
  - Mentor Agent: Explains concepts in multiple modes
  - Interviewer Agent: Simulates real interviews
  - Reviewer Agent: Analyzes performance and adapts roadmap

- 🎯 **Interview-Aware Roadmaps**
  - Every topic includes "Why interviewers ask this"
  - Common interview questions
  - Red flags to avoid
  
- 📊 **Adaptive Learning System**
  - Continuously adjusts based on your progress
  - Performance-based difficulty adjustment
  - Automatic gap identification

- 🏗️ **Project-Driven Learning**
  - Real-world, resume-worthy projects
  - Progressive complexity
  - Portfolio building

- 🏢 **Company-Specific Preparation**
  - Different modes for TCS, Infosys, Product companies, Startups
  - Customized interview patterns
  - Role-specific focus areas

## 📁 Project Structure

```
AI Career Roadmap Generator/
├── architecture/              # Architecture documentation & diagrams
│   ├── images/               # All architecture diagrams (PNG)
│   ├── *.py                  # Python scripts to generate diagrams
│   └── *.md                  # Documentation files
├── INDEX.md                  # Project overview
└── README.md                 # This file
```

## 🎨 Architecture Diagrams

We have 5 comprehensive architecture diagrams:

1. **System Architecture** - Complete technical stack
2. **User Journey** - User experience flow
3. **AI Agent Architecture** - 4 specialized AI agents
4. **Roadmap Generation Flow** - AI roadmap creation process
5. **Data Flow Diagram** - Data movement through system

All diagrams are in `architecture/images/` folder (300 DPI, print-quality).

## 📚 Documentation

- **[PROJECT_DOCUMENTATION.md](architecture/PROJECT_DOCUMENTATION.md)** - Complete technical documentation
- **[PRESENTATION_GUIDE.md](architecture/PRESENTATION_GUIDE.md)** - Presentation materials and pitch guide
- **[README.md](architecture/README.md)** - Architecture overview
- **[INDEX.md](INDEX.md)** - Quick start guide

## 💻 Technology Stack

### Frontend
- React 18 + Next.js 14
- Tailwind CSS + shadcn/ui
- Zustand/Redux Toolkit

### Backend
- Node.js 20+ with TypeScript
- Express.js or Fastify
- RESTful API + GraphQL (optional)

### AI & ML
- OpenAI GPT-4 or Anthropic Claude
- LangChain for orchestration
- Pinecone/ChromaDB for vector storage

### Databases
- PostgreSQL (user data)
- MongoDB (roadmaps)
- Redis (cache)
- Pinecone/Chroma (embeddings)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ (for diagram generation)
- Node.js 20+ (for future development)
- Git

### View Documentation
```bash
cd architecture
# Open PROJECT_DOCUMENTATION.md in your editor
```

### Regenerate Diagrams
```bash
cd architecture
python generate_system_architecture.py
python generate_user_journey.py
python generate_ai_agents.py
python generate_roadmap_flow.py
python generate_data_flow.py
```

## 📊 What Makes This Different?

| Feature | Our Platform | Competitors |
|---------|-------------|-------------|
| Personalization | ✅ AI-driven | ❌ Template-based |
| Adaptation | ✅ Real-time | ❌ Static |
| Interview Prep | ✅ Integrated & intelligent | ⚠️ Generic |
| AI Agents | ✅ 4 specialized agents | ❌ None |
| Projects | ✅ Personalized suggestions | ❌ Generic lists |
| Company-Specific | ✅ Multiple modes | ❌ One-size-fits-all |

## 🎯 Roadmap

### Phase 1: Foundation (Weeks 1-2)
- [ ] Frontend setup (Next.js)
- [ ] Backend setup (Node.js)
- [ ] Database configuration
- [ ] Authentication system

### Phase 2: Core Features (Weeks 3-5)
- [ ] User profile creation
- [ ] AI Planner Agent
- [ ] Roadmap generation
- [ ] Dashboard UI

### Phase 3: AI Agents (Weeks 6-8)
- [ ] Mentor Agent
- [ ] Interviewer Agent
- [ ] Reviewer Agent
- [ ] LLM integration

### Phase 4: Advanced Features (Weeks 9-10)
- [ ] Adaptive engine
- [ ] Company-specific modes
- [ ] Project suggestions
- [ ] Analytics

### Phase 5: Polish & Deploy (Weeks 11-12)
- [ ] Testing
- [ ] UI/UX refinement
- [ ] Performance optimization
- [ ] Deployment

## 📈 Expected Impact

- **75% interview success rate** (vs 40% industry average)
- **4-6 months** to job-ready
- **Personalized** learning path
- **Portfolio** of real projects

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines (coming soon).

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Raghuram** - *Initial work* - [Raghuram777](https://github.com/Raghuram777)

## 🙏 Acknowledgments

- Inspired by the need for personalized career development
- Built with modern AI technologies
- Designed to help millions achieve their career goals

---

**Status**: Architecture & Documentation Complete ✅  
**Next**: Development starts now! 🚀

For detailed information, check out the [complete documentation](architecture/PROJECT_DOCUMENTATION.md).
