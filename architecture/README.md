# Architecture Documentation

This folder contains comprehensive architecture documentation for the **AI Career Roadmap Generator** project.

## 📁 Contents

### 📄 Documentation Files

1. **[PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md)** - Complete project documentation
   - Detailed project overview
   - System architecture explanation
   - AI intelligence components
   - Technology stack details
   - Database design schemas
   - API architecture
   - Implementation roadmap

### 🖼️ Architecture Diagrams

All diagrams are located in the `images/` folder and are generated as high-resolution PNG files (300 DPI).

#### 1. System Architecture Diagram
**File**: `images/01_system_architecture.png`

Shows the complete system architecture including:
- Frontend Layer (React/Next.js)
- API Gateway (Node.js/Express)
- Backend Services (User Management, Roadmap, Interview)
- AI Orchestration Layer
- Four AI Agents (Planner, Mentor, Interviewer, Reviewer)
- LLM Provider Integration
- Database Layer (PostgreSQL, MongoDB, Redis, Vector DB)

**Use in presentation**: Opening slide to show overall technical architecture

---

#### 2. User Journey Flowchart
**File**: `images/02_user_journey.png`

Illustrates the complete user experience flow:
- Start: User opens app
- Authentication (Login/Signup)
- Profile creation with AI onboarding
- AI profile analysis
- Roadmap generation
- Learning loop (Learn, Practice, Complete)
- Mock interviews and progress tracking
- AI-powered adaptation
- Final assessment and interview readiness

**Use in presentation**: To explain how users interact with the system

---

#### 3. AI Agent Architecture
**File**: `images/03_ai_agent_architecture.png`

Detailed view of the Agentic AI system:
- **Central Orchestrator**: Routes requests and manages context
- **Planner Agent**: Designs personalized roadmaps
- **Mentor Agent**: Explains concepts in multiple teaching modes
- **Interviewer Agent**: Conducts mock interviews
- **Reviewer Agent**: Evaluates performance and adapts roadmap
- **Shared Resources**: LLM Engine, Memory System, Tool Library
- **Inter-agent Communication**: How agents collaborate

**Use in presentation**: To showcase the advanced AI capabilities

---

#### 4. Roadmap Generation Flow
**File**: `images/04_roadmap_generation_flow.png`

Step-by-step process of how AI generates roadmaps:
1. User Profile Input (education, experience, target role, etc.)
2. AI Profile Analysis by Planner Agent
3. Role-Specific Template Selection
4. AI-Powered Customization
5. Phase Construction (Foundation → Core → Advanced → Projects → Interview Prep)
6. AI Enhancement Layer (interview questions, tips, red flags)
7. Topic Dependency Resolution
8. Intelligent Timeline Allocation
9. Final Roadmap Generation with multiple output formats

**Use in presentation**: To demonstrate the intelligent roadmap creation process

---

#### 5. Data Flow Diagram
**File**: `images/05_data_flow_diagram.png`

Shows how data moves through the system:
- **External Entity**: User interactions
- **Processes**:
  - P1: Authentication
  - P2: Profile Creation
  - P3: AI Analysis
  - P4: Roadmap Generation
  - P5: Display Dashboard
  - P6: Learning Session
  - P7: AI Mentor
  - P8: Mock Interview
  - P9: Progress Update
  - P10: Adaptive Engine
- **Data Stores**: User DB, Knowledge Base, Roadmap Store, Vector DB, Cache
- **Data Flows**: All arrows showing data movement between components

**Use in presentation**: To explain data architecture and information flow

---

## 🔄 Regenerating Diagrams

If you need to modify or regenerate any diagram:

### Prerequisites
```bash
pip install matplotlib
```

### Generate Individual Diagrams

```bash
# System Architecture
python generate_system_architecture.py

# User Journey
python generate_user_journey.py

# AI Agent Architecture
python generate_ai_agents.py

# Roadmap Generation Flow
python generate_roadmap_flow.py

# Data Flow Diagram
python generate_data_flow.py
```

### Generate All Diagrams
```bash
# Windows PowerShell
cd "d:\AI Career Roadmap Generator\architecture"
python generate_system_architecture.py
python generate_user_journey.py
python generate_ai_agents.py
python generate_roadmap_flow.py
python generate_data_flow.py
```

---

## 📊 Diagram Specifications

All diagrams are:
- **Format**: PNG
- **Resolution**: 300 DPI (print-quality)
- **Background**: White
- **Color-coded**: Different colors for different component types
- **High-contrast**: Suitable for both presentations and documents

### Color Scheme

- **Frontend**: Light Blue (#E3F2FD)
- **Backend**: Light Orange (#FFF3E0)
- **AI Components**: Light Purple (#F3E5F5)
- **Databases**: Light Green (#E8F5E9)
- **External Services**: Light Red (#FFEBEE)

---

## 📝 Presentation Guidelines

### Recommended Order

1. **Start with**: System Architecture (01) - Show the big picture
2. **Then show**: User Journey (02) - Explain user experience
3. **Deep dive**: AI Agent Architecture (03) - Highlight intelligent features
4. **Explain process**: Roadmap Generation Flow (04) - Show the magic
5. **Technical details**: Data Flow Diagram (05) - For technical audience

### Key Points to Emphasize

1. **AI-Driven Intelligence**
   - Multiple specialized AI agents
   - Not just a template-based system
   - Continuous adaptation

2. **User-Centric Design**
   - Personalized learning paths
   - Interview-focused preparation
   - Project-driven approach

3. **Scalable Architecture**
   - Microservices design
   - Independent scaling
   - Cloud-ready

4. **Advanced Features**
   - Agentic AI system
   - Multi-agent collaboration
   - Company-specific preparation modes

---

## 🎯 For Developers

### Modifying Diagrams

Each Python script is well-commented and structured. To modify:

1. Open the relevant `generate_*.py` file
2. Modify the code (colors, text, layout)
3. Run the script to regenerate
4. Check the output in `images/` folder

### Adding New Diagrams

1. Create a new Python script (e.g., `generate_new_diagram.py`)
2. Use matplotlib and follow the existing structure
3. Save output to `images/` folder with appropriate naming
4. Update this README

---

## 📧 Questions?

Refer to the [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md) for complete technical details.

---

**Last Updated**: January 5, 2026  
**Version**: 1.0
