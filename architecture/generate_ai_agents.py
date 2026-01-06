"""
Generate AI Agent Architecture Diagram for AI Career Roadmap Generator
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

def create_ai_agent_architecture():
    fig, ax = plt.subplots(figsize=(16, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(5, 11.5, 'AI Agent Architecture - Agentic System', 
            fontsize=20, fontweight='bold', ha='center')
    
    # Colors
    orchestrator_color = '#673AB7'
    agent_color = '#9C27B0'
    llm_color = '#E91E63'
    memory_color = '#00BCD4'
    tool_color = '#4CAF50'
    
    # Central Orchestrator
    orchestrator_box = FancyBboxPatch((3.5, 9), 3, 1.5, 
                                      boxstyle="round,pad=0.15", 
                                      edgecolor='black', facecolor=orchestrator_color, 
                                      linewidth=3)
    ax.add_patch(orchestrator_box)
    ax.text(5, 10.2, '🎯 AI Orchestrator', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(5, 9.9, 'Central Coordinator', fontsize=10, ha='center', color='white')
    ax.text(5, 9.65, '• Route requests to agents', fontsize=9, ha='center', color='white')
    ax.text(5, 9.45, '• Manage context & memory', fontsize=9, ha='center', color='white')
    ax.text(5, 9.25, '• Coordinate multi-agent tasks', fontsize=9, ha='center', color='white')
    
    # ===== Four Main Agents =====
    
    # 1. Planner Agent (Top Left)
    planner_agent = FancyBboxPatch((0.3, 6.5), 2.2, 2, 
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='black', facecolor=agent_color, 
                                   linewidth=2)
    ax.add_patch(planner_agent)
    ax.text(1.4, 8.2, '📋 Planner Agent', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(1.4, 7.95, 'Roadmap Architect', fontsize=9, ha='center', color='white', style='italic')
    
    ax.text(1.4, 7.65, 'Capabilities:', fontsize=9, fontweight='bold', ha='center', color='white')
    ax.text(1.4, 7.45, '• Analyze user profile', fontsize=8, ha='center', color='white')
    ax.text(1.4, 7.28, '• Identify skill gaps', fontsize=8, ha='center', color='white')
    ax.text(1.4, 7.11, '• Design learning phases', fontsize=8, ha='center', color='white')
    ax.text(1.4, 6.94, '• Set milestones', fontsize=8, ha='center', color='white')
    ax.text(1.4, 6.77, '• Prioritize topics', fontsize=8, ha='center', color='white')
    ax.text(1.4, 6.60, '• Suggest projects', fontsize=8, ha='center', color='white')
    
    # 2. Mentor Agent (Top Right)
    mentor_agent = FancyBboxPatch((7.5, 6.5), 2.2, 2, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='black', facecolor=agent_color, 
                                  linewidth=2)
    ax.add_patch(mentor_agent)
    ax.text(8.6, 8.2, '👨‍🏫 Mentor Agent', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(8.6, 7.95, 'Knowledge Explainer', fontsize=9, ha='center', color='white', style='italic')
    
    ax.text(8.6, 7.65, 'Capabilities:', fontsize=9, fontweight='bold', ha='center', color='white')
    ax.text(8.6, 7.45, '• Explain concepts', fontsize=8, ha='center', color='white')
    ax.text(8.6, 7.28, '• Simplify complex topics', fontsize=8, ha='center', color='white')
    ax.text(8.6, 7.11, '• Provide analogies', fontsize=8, ha='center', color='white')
    ax.text(8.6, 6.94, '• Answer queries', fontsize=8, ha='center', color='white')
    ax.text(8.6, 6.77, '• Multi-mode teaching', fontsize=8, ha='center', color='white')
    ax.text(8.6, 6.60, '• Adaptive explanations', fontsize=8, ha='center', color='white')
    
    # 3. Interviewer Agent (Bottom Left)
    interviewer_agent = FancyBboxPatch((0.3, 3.5), 2.2, 2, 
                                       boxstyle="round,pad=0.1", 
                                       edgecolor='black', facecolor=agent_color, 
                                       linewidth=2)
    ax.add_patch(interviewer_agent)
    ax.text(1.4, 5.2, '🎤 Interviewer Agent', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(1.4, 4.95, 'Mock Interviewer', fontsize=9, ha='center', color='white', style='italic')
    
    ax.text(1.4, 4.65, 'Capabilities:', fontsize=9, fontweight='bold', ha='center', color='white')
    ax.text(1.4, 4.45, '• Generate questions', fontsize=8, ha='center', color='white')
    ax.text(1.4, 4.28, '• Probe deeper', fontsize=8, ha='center', color='white')
    ax.text(1.4, 4.11, '• Simulate real scenarios', fontsize=8, ha='center', color='white')
    ax.text(1.4, 3.94, '• Behavioral questions', fontsize=8, ha='center', color='white')
    ax.text(1.4, 3.77, '• Technical challenges', fontsize=8, ha='center', color='white')
    ax.text(1.4, 3.60, '• Company-specific prep', fontsize=8, ha='center', color='white')
    
    # 4. Reviewer Agent (Bottom Right)
    reviewer_agent = FancyBboxPatch((7.5, 3.5), 2.2, 2, 
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='black', facecolor=agent_color, 
                                    linewidth=2)
    ax.add_patch(reviewer_agent)
    ax.text(8.6, 5.2, '📊 Reviewer Agent', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(8.6, 4.95, 'Performance Analyzer', fontsize=9, ha='center', color='white', style='italic')
    
    ax.text(8.6, 4.65, 'Capabilities:', fontsize=9, fontweight='bold', ha='center', color='white')
    ax.text(8.6, 4.45, '• Evaluate answers', fontsize=8, ha='center', color='white')
    ax.text(8.6, 4.28, '• Provide feedback', fontsize=8, ha='center', color='white')
    ax.text(8.6, 4.11, '• Identify weak areas', fontsize=8, ha='center', color='white')
    ax.text(8.6, 3.94, '• Suggest improvements', fontsize=8, ha='center', color='white')
    ax.text(8.6, 3.77, '• Adapt roadmap', fontsize=8, ha='center', color='white')
    ax.text(8.6, 3.60, '• Track progress', fontsize=8, ha='center', color='white')
    
    # Connections from Orchestrator to Agents
    arrow1 = FancyArrowPatch((3.8, 9.5), (2.5, 8.2),
                             arrowstyle='<->', mutation_scale=20, 
                             linewidth=2.5, color='#424242')
    ax.add_patch(arrow1)
    
    arrow2 = FancyArrowPatch((6.2, 9.5), (7.5, 8.2),
                             arrowstyle='<->', mutation_scale=20, 
                             linewidth=2.5, color='#424242')
    ax.add_patch(arrow2)
    
    arrow3 = FancyArrowPatch((3.8, 9.2), (2.5, 5.3),
                             arrowstyle='<->', mutation_scale=20, 
                             linewidth=2.5, color='#424242')
    ax.add_patch(arrow3)
    
    arrow4 = FancyArrowPatch((6.2, 9.2), (7.5, 5.3),
                             arrowstyle='<->', mutation_scale=20, 
                             linewidth=2.5, color='#424242')
    ax.add_patch(arrow4)
    
    # Shared Resources at Bottom
    
    # LLM Engine
    llm_box = FancyBboxPatch((1.5, 1.5), 2.5, 1.2, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='black', facecolor=llm_color, 
                             linewidth=2)
    ax.add_patch(llm_box)
    ax.text(2.75, 2.4, '🧠 LLM Engine', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(2.75, 2.15, 'GPT-4 / Claude', fontsize=9, ha='center', color='white')
    ax.text(2.75, 1.92, '• Natural language reasoning', fontsize=8, ha='center', color='white')
    ax.text(2.75, 1.72, '• Context understanding', fontsize=8, ha='center', color='white')
    
    # Memory System
    memory_box = FancyBboxPatch((4.5, 1.5), 2, 1.2, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='black', facecolor=memory_color, 
                                linewidth=2)
    ax.add_patch(memory_box)
    ax.text(5.5, 2.4, '💾 Memory System', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5.5, 2.15, 'Context Storage', fontsize=9, ha='center', color='white')
    ax.text(5.5, 1.92, '• Conversation history', fontsize=8, ha='center', color='white')
    ax.text(5.5, 1.72, '• User profile data', fontsize=8, ha='center', color='white')
    
    # Tool Library
    tool_box = FancyBboxPatch((7, 1.5), 2.5, 1.2, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='black', facecolor=tool_color, 
                              linewidth=2)
    ax.add_patch(tool_box)
    ax.text(8.25, 2.4, '🛠️ Tool Library', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(8.25, 2.15, 'Agent Tools', fontsize=9, ha='center', color='white')
    ax.text(8.25, 1.92, '• Knowledge base access', fontsize=8, ha='center', color='white')
    ax.text(8.25, 1.72, '• Code execution', fontsize=8, ha='center', color='white')
    
    # Connections from Agents to Shared Resources
    # All agents connect to LLM
    ax.plot([1.4, 1.4, 2.75], [3.5, 2.7, 2.7], 'k--', linewidth=1.5, alpha=0.6)
    ax.plot([8.6, 8.6, 2.75], [3.5, 2.7, 2.7], 'k--', linewidth=1.5, alpha=0.6)
    
    # All agents connect to Memory
    ax.plot([1.4, 1.4, 5.5], [3.5, 3, 3], 'k--', linewidth=1.5, alpha=0.6)
    ax.plot([1.4, 1.4, 5.5], [6.5, 3, 3], 'k--', linewidth=1.5, alpha=0.6)
    ax.plot([8.6, 8.6, 5.5], [3.5, 3, 3], 'k--', linewidth=1.5, alpha=0.6)
    ax.plot([8.6, 8.6, 5.5], [6.5, 3, 3], 'k--', linewidth=1.5, alpha=0.6)
    
    # All agents connect to Tools
    ax.plot([8.6, 8.6, 8.25], [6.5, 2.7, 2.7], 'k--', linewidth=1.5, alpha=0.6)
    ax.plot([1.4, 1.4, 8.25], [6.5, 0.8, 0.8], 'k--', linewidth=1.5, alpha=0.6)
    ax.plot([8.25, 8.25], [0.8, 1.5], 'k--', linewidth=1.5, alpha=0.6)
    
    # Agent Communication
    ax.text(5, 5.8, '⟷', fontsize=30, ha='center', color='#FF6B6B')
    ax.text(5, 5.3, 'Inter-Agent', fontsize=9, ha='center', fontweight='bold')
    ax.text(5, 5.05, 'Communication', fontsize=9, ha='center', fontweight='bold')
    
    # Communication lines between agents
    ax.plot([2.5, 7.5], [7.5, 7.5], 'r--', linewidth=1.5, alpha=0.5)
    ax.plot([2.5, 7.5], [4.5, 4.5], 'r--', linewidth=1.5, alpha=0.5)
    ax.plot([2.5, 2.5], [5.5, 8.5], 'r--', linewidth=1.5, alpha=0.5)
    ax.plot([7.5, 7.5], [5.5, 8.5], 'r--', linewidth=1.5, alpha=0.5)
    
    # Example Flow
    flow_box = FancyBboxPatch((3, 0.3), 4, 0.8, 
                              boxstyle="round,pad=0.05", 
                              edgecolor='#FF9800', facecolor='#FFF8E1', 
                              linewidth=2)
    ax.add_patch(flow_box)
    ax.text(5, 0.85, '📝 Example: "Generate roadmap for SDE role"', fontsize=10, fontweight='bold', ha='center')
    ax.text(5, 0.60, '1. Orchestrator → Planner Agent (design roadmap) → 2. Reviewer Agent (validate)', fontsize=8, ha='center')
    ax.text(5, 0.40, '3. Mentor Agent (explain concepts) → 4. Interviewer Agent (test knowledge)', fontsize=8, ha='center')
    
    plt.tight_layout()
    plt.savefig('d:/AI Career Roadmap Generator/architecture/images/03_ai_agent_architecture.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ AI Agent Architecture diagram generated successfully!")

if __name__ == "__main__":
    create_ai_agent_architecture()
