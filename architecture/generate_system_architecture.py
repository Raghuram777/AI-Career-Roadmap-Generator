"""
Generate System Architecture Diagram for AI Career Roadmap Generator
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

def create_system_architecture():
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'AI Career Roadmap Generator - System Architecture', 
            fontsize=20, fontweight='bold', ha='center')
    
    # Color scheme
    frontend_color = '#E3F2FD'
    backend_color = '#FFF3E0'
    ai_color = '#F3E5F5'
    db_color = '#E8F5E9'
    external_color = '#FFEBEE'
    
    # Frontend Layer
    frontend_box = FancyBboxPatch((0.5, 7), 2.5, 1.5, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#1976D2', facecolor=frontend_color, 
                                  linewidth=2)
    ax.add_patch(frontend_box)
    ax.text(1.75, 8.2, 'Frontend Layer', fontsize=12, fontweight='bold', ha='center')
    ax.text(1.75, 7.85, 'React/Next.js', fontsize=9, ha='center')
    ax.text(1.75, 7.6, '• Dashboard UI', fontsize=8, ha='center')
    ax.text(1.75, 7.4, '• Progress Visualizer', fontsize=8, ha='center')
    ax.text(1.75, 7.2, '• AI Chat Interface', fontsize=8, ha='center')
    
    # API Gateway
    gateway_box = FancyBboxPatch((3.75, 7), 2.5, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#F57C00', facecolor=backend_color, 
                                 linewidth=2)
    ax.add_patch(gateway_box)
    ax.text(5, 8.2, 'API Gateway', fontsize=12, fontweight='bold', ha='center')
    ax.text(5, 7.85, 'Node.js/Express', fontsize=9, ha='center')
    ax.text(5, 7.6, '• Authentication', fontsize=8, ha='center')
    ax.text(5, 7.4, '• Request Router', fontsize=8, ha='center')
    ax.text(5, 7.2, '• Rate Limiting', fontsize=8, ha='center')
    
    # User Management Service
    user_service = FancyBboxPatch((0.5, 5), 1.8, 1.3, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#F57C00', facecolor=backend_color, 
                                  linewidth=2)
    ax.add_patch(user_service)
    ax.text(1.4, 5.95, 'User Management', fontsize=10, fontweight='bold', ha='center')
    ax.text(1.4, 5.65, '• Profile CRUD', fontsize=8, ha='center')
    ax.text(1.4, 5.45, '• Auth Service', fontsize=8, ha='center')
    ax.text(1.4, 5.25, '• Progress Track', fontsize=8, ha='center')
    
    # Roadmap Service
    roadmap_service = FancyBboxPatch((2.6, 5), 1.8, 1.3, 
                                     boxstyle="round,pad=0.1", 
                                     edgecolor='#F57C00', facecolor=backend_color, 
                                     linewidth=2)
    ax.add_patch(roadmap_service)
    ax.text(3.5, 5.95, 'Roadmap Service', fontsize=10, fontweight='bold', ha='center')
    ax.text(3.5, 5.65, '• Generate', fontsize=8, ha='center')
    ax.text(3.5, 5.45, '• Adapt', fontsize=8, ha='center')
    ax.text(3.5, 5.25, '• Persist', fontsize=8, ha='center')
    
    # Interview Service
    interview_service = FancyBboxPatch((4.7, 5), 1.8, 1.3, 
                                       boxstyle="round,pad=0.1", 
                                       edgecolor='#F57C00', facecolor=backend_color, 
                                       linewidth=2)
    ax.add_patch(interview_service)
    ax.text(5.6, 5.95, 'Interview Service', fontsize=10, fontweight='bold', ha='center')
    ax.text(5.6, 5.65, '• Mock Tests', fontsize=8, ha='center')
    ax.text(5.6, 5.45, '• Q&A Engine', fontsize=8, ha='center')
    ax.text(5.6, 5.25, '• Evaluation', fontsize=8, ha='center')
    
    # AI Orchestrator
    ai_orchestrator = FancyBboxPatch((6.8, 5), 2.7, 1.3, 
                                     boxstyle="round,pad=0.1", 
                                     edgecolor='#7B1FA2', facecolor=ai_color, 
                                     linewidth=3)
    ax.add_patch(ai_orchestrator)
    ax.text(8.15, 5.95, 'AI Orchestration Layer', fontsize=11, fontweight='bold', ha='center')
    ax.text(8.15, 5.65, '• Prompt Engineering', fontsize=8, ha='center')
    ax.text(8.15, 5.45, '• Context Management', fontsize=8, ha='center')
    ax.text(8.15, 5.25, '• Agent Coordinator', fontsize=8, ha='center')
    
    # AI Agents Layer
    planner_agent = FancyBboxPatch((0.5, 2.8), 1.5, 1.3, 
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#7B1FA2', facecolor=ai_color, 
                                   linewidth=2)
    ax.add_patch(planner_agent)
    ax.text(1.25, 3.75, 'Planner Agent', fontsize=10, fontweight='bold', ha='center')
    ax.text(1.25, 3.5, '• Analyze Profile', fontsize=8, ha='center')
    ax.text(1.25, 3.3, '• Build Roadmap', fontsize=8, ha='center')
    ax.text(1.25, 3.1, '• Set Milestones', fontsize=8, ha='center')
    
    mentor_agent = FancyBboxPatch((2.3, 2.8), 1.5, 1.3, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#7B1FA2', facecolor=ai_color, 
                                  linewidth=2)
    ax.add_patch(mentor_agent)
    ax.text(3.05, 3.75, 'Mentor Agent', fontsize=10, fontweight='bold', ha='center')
    ax.text(3.05, 3.5, '• Explain Topics', fontsize=8, ha='center')
    ax.text(3.05, 3.3, '• Chat Support', fontsize=8, ha='center')
    ax.text(3.05, 3.1, '• Multi-mode', fontsize=8, ha='center')
    
    interviewer_agent = FancyBboxPatch((4.1, 2.8), 1.5, 1.3, 
                                       boxstyle="round,pad=0.1", 
                                       edgecolor='#7B1FA2', facecolor=ai_color, 
                                       linewidth=2)
    ax.add_patch(interviewer_agent)
    ax.text(4.85, 3.75, 'Interviewer Agent', fontsize=10, fontweight='bold', ha='center')
    ax.text(4.85, 3.5, '• Ask Questions', fontsize=8, ha='center')
    ax.text(4.85, 3.3, '• Probe Deeper', fontsize=8, ha='center')
    ax.text(4.85, 3.1, '• Simulate Real', fontsize=8, ha='center')
    
    reviewer_agent = FancyBboxPatch((5.9, 2.8), 1.5, 1.3, 
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='#7B1FA2', facecolor=ai_color, 
                                    linewidth=2)
    ax.add_patch(reviewer_agent)
    ax.text(6.65, 3.75, 'Reviewer Agent', fontsize=10, fontweight='bold', ha='center')
    ax.text(6.65, 3.5, '• Analyze Answers', fontsize=8, ha='center')
    ax.text(6.65, 3.3, '• Give Feedback', fontsize=8, ha='center')
    ax.text(6.65, 3.1, '• Adapt Roadmap', fontsize=8, ha='center')
    
    # LLM Provider
    llm_provider = FancyBboxPatch((7.7, 2.8), 1.8, 1.3, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#C62828', facecolor=external_color, 
                                  linewidth=2)
    ax.add_patch(llm_provider)
    ax.text(8.6, 3.75, 'LLM Provider', fontsize=10, fontweight='bold', ha='center')
    ax.text(8.6, 3.5, 'OpenAI API', fontsize=9, ha='center')
    ax.text(8.6, 3.25, 'GPT-4/Claude', fontsize=8, ha='center')
    ax.text(8.6, 3.05, '• Reasoning', fontsize=8, ha='center')
    
    # Database Layer
    user_db = FancyBboxPatch((0.5, 0.8), 1.8, 1.2, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#388E3C', facecolor=db_color, 
                             linewidth=2)
    ax.add_patch(user_db)
    ax.text(1.4, 1.65, 'User Database', fontsize=10, fontweight='bold', ha='center')
    ax.text(1.4, 1.4, 'PostgreSQL/MongoDB', fontsize=8, ha='center')
    ax.text(1.4, 1.2, '• User Profiles', fontsize=8, ha='center')
    ax.text(1.4, 1.0, '• Auth Data', fontsize=8, ha='center')
    
    roadmap_db = FancyBboxPatch((2.6, 0.8), 1.8, 1.2, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#388E3C', facecolor=db_color, 
                                linewidth=2)
    ax.add_patch(roadmap_db)
    ax.text(3.5, 1.65, 'Roadmap Store', fontsize=10, fontweight='bold', ha='center')
    ax.text(3.5, 1.4, 'MongoDB', fontsize=8, ha='center')
    ax.text(3.5, 1.2, '• Roadmaps', fontsize=8, ha='center')
    ax.text(3.5, 1.0, '• Progress', fontsize=8, ha='center')
    
    cache_db = FancyBboxPatch((4.7, 0.8), 1.8, 1.2, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#388E3C', facecolor=db_color, 
                              linewidth=2)
    ax.add_patch(cache_db)
    ax.text(5.6, 1.65, 'Cache Layer', fontsize=10, fontweight='bold', ha='center')
    ax.text(5.6, 1.4, 'Redis', fontsize=8, ha='center')
    ax.text(5.6, 1.2, '• Sessions', fontsize=8, ha='center')
    ax.text(5.6, 1.0, '• AI Context', fontsize=8, ha='center')
    
    vector_db = FancyBboxPatch((6.7, 0.8), 2.3, 1.2, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#388E3C', facecolor=db_color, 
                               linewidth=2)
    ax.add_patch(vector_db)
    ax.text(7.85, 1.65, 'Vector Database', fontsize=10, fontweight='bold', ha='center')
    ax.text(7.85, 1.4, 'Pinecone/Chroma', fontsize=8, ha='center')
    ax.text(7.85, 1.2, '• Interview Q&A', fontsize=8, ha='center')
    ax.text(7.85, 1.0, '• Embeddings', fontsize=8, ha='center')
    
    # Arrows - Frontend to Gateway
    arrow1 = FancyArrowPatch((3, 7.75), (3.75, 7.75),
                             arrowstyle='->', mutation_scale=20, 
                             linewidth=2, color='#424242')
    ax.add_patch(arrow1)
    
    # Gateway to Services
    arrow2 = FancyArrowPatch((5, 7), (1.4, 6.3),
                             arrowstyle='->', mutation_scale=15, 
                             linewidth=1.5, color='#424242')
    ax.add_patch(arrow2)
    
    arrow3 = FancyArrowPatch((5, 7), (3.5, 6.3),
                             arrowstyle='->', mutation_scale=15, 
                             linewidth=1.5, color='#424242')
    ax.add_patch(arrow3)
    
    arrow4 = FancyArrowPatch((5, 7), (5.6, 6.3),
                             arrowstyle='->', mutation_scale=15, 
                             linewidth=1.5, color='#424242')
    ax.add_patch(arrow4)
    
    # Services to AI Orchestrator
    arrow5 = FancyArrowPatch((6.5, 5.65), (6.8, 5.65),
                             arrowstyle='<->', mutation_scale=15, 
                             linewidth=2, color='#7B1FA2')
    ax.add_patch(arrow5)
    
    # AI Orchestrator to Agents
    arrow6 = FancyArrowPatch((8.15, 5), (1.25, 4.1),
                             arrowstyle='<->', mutation_scale=15, 
                             linewidth=1.5, color='#7B1FA2')
    ax.add_patch(arrow6)
    
    arrow7 = FancyArrowPatch((8.15, 5), (3.05, 4.1),
                             arrowstyle='<->', mutation_scale=15, 
                             linewidth=1.5, color='#7B1FA2')
    ax.add_patch(arrow7)
    
    arrow8 = FancyArrowPatch((8.15, 5), (4.85, 4.1),
                             arrowstyle='<->', mutation_scale=15, 
                             linewidth=1.5, color='#7B1FA2')
    ax.add_patch(arrow8)
    
    arrow9 = FancyArrowPatch((8.15, 5), (6.65, 4.1),
                             arrowstyle='<->', mutation_scale=15, 
                             linewidth=1.5, color='#7B1FA2')
    ax.add_patch(arrow9)
    
    # Agents to LLM
    arrow10 = FancyArrowPatch((7.4, 3.45), (7.7, 3.45),
                              arrowstyle='<->', mutation_scale=15, 
                              linewidth=2, color='#C62828')
    ax.add_patch(arrow10)
    
    # Services to Databases
    arrow11 = FancyArrowPatch((1.4, 5), (1.4, 2),
                              arrowstyle='<->', mutation_scale=15, 
                              linewidth=1.5, color='#388E3C')
    ax.add_patch(arrow11)
    
    arrow12 = FancyArrowPatch((3.5, 5), (3.5, 2),
                              arrowstyle='<->', mutation_scale=15, 
                              linewidth=1.5, color='#388E3C')
    ax.add_patch(arrow12)
    
    arrow13 = FancyArrowPatch((5.6, 5), (5.6, 2),
                              arrowstyle='<->', mutation_scale=15, 
                              linewidth=1.5, color='#388E3C')
    ax.add_patch(arrow13)
    
    # Legend
    legend_y = 0.3
    ax.text(0.5, legend_y, 'Legend:', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('d:/AI Career Roadmap Generator/architecture/images/01_system_architecture.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ System Architecture diagram generated successfully!")

if __name__ == "__main__":
    create_system_architecture()
