"""
Generate Roadmap Generation Flow Diagram for AI Career Roadmap Generator
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def create_roadmap_generation_flow():
    fig, ax = plt.subplots(figsize=(15, 16))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 17)
    ax.axis('off')
    
    # Title
    ax.text(5, 16.5, 'AI Roadmap Generation Flow - Detailed Process', 
            fontsize=20, fontweight='bold', ha='center')
    
    # Colors
    input_color = '#E3F2FD'
    process_color = '#C5CAE9'
    ai_color = '#F3E5F5'
    output_color = '#C8E6C9'
    
    y_pos = 15.5
    
    # Step 1: Input Collection
    input_box = FancyBboxPatch((0.5, y_pos-0.6), 9, 0.8, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#1976D2', facecolor=input_color, 
                               linewidth=2)
    ax.add_patch(input_box)
    ax.text(5, y_pos-0.05, 'Step 1: User Profile Input', fontsize=12, fontweight='bold', ha='center')
    ax.text(5, y_pos-0.3, 'Education • Experience • Skills • Target Role • Target Company • Timeline • Comfort Level', 
            fontsize=9, ha='center')
    
    ax.arrow(5, y_pos-0.6, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 1.5
    
    # Step 2: Profile Analysis
    analysis_box = FancyBboxPatch((1, y_pos-0.8), 8, 1.3, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#7B1FA2', facecolor=ai_color, 
                                  linewidth=3)
    ax.add_patch(analysis_box)
    ax.text(5, y_pos, 'Step 2: AI Profile Analysis (Planner Agent)', fontsize=12, fontweight='bold', ha='center')
    
    # Sub-steps
    ax.text(5, y_pos-0.25, '✓ Skill Gap Identification', fontsize=9, ha='center')
    ax.text(5, y_pos-0.40, '✓ Experience Level Assessment', fontsize=9, ha='center')
    ax.text(5, y_pos-0.55, '✓ Learning Style Detection', fontsize=9, ha='center')
    
    ax.arrow(5, y_pos-0.8, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 1.7
    
    # Step 3: Role Template Selection
    template_box = FancyBboxPatch((1.5, y_pos-0.6), 7, 1, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#5E35B1', facecolor=process_color, 
                                  linewidth=2)
    ax.add_patch(template_box)
    ax.text(5, y_pos, 'Step 3: Role-Specific Template Selection', fontsize=12, fontweight='bold', ha='center')
    
    # Role examples
    ax.text(2.5, y_pos-0.3, 'SDE:\nDSA + System Design', fontsize=8, ha='center', 
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(5, y_pos-0.3, 'AI Engineer:\nML → DL → LLMs', fontsize=8, ha='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(7.5, y_pos-0.3, 'Full Stack:\nFE + BE + DB', fontsize=8, ha='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    ax.arrow(5, y_pos-0.6, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 1.5
    
    # Step 4: Customization
    customize_box = FancyBboxPatch((0.8, y_pos-1), 8.4, 1.6, 
                                   boxstyle="round,pad=0.1", 
                                   edgecolor='#7B1FA2', facecolor=ai_color, 
                                   linewidth=3)
    ax.add_patch(customize_box)
    ax.text(5, y_pos, 'Step 4: AI-Powered Customization', fontsize=12, fontweight='bold', ha='center')
    
    ax.text(5, y_pos-0.28, '🎯 Adjust Difficulty Based on Experience', fontsize=9, ha='center')
    ax.text(5, y_pos-0.48, '📊 Prioritize Topics Based on Target Company', fontsize=9, ha='center')
    ax.text(5, y_pos-0.68, '⏱️ Timeline Optimization (3/6/12 months)', fontsize=9, ha='center')
    ax.text(5, y_pos-0.88, '🔍 Add Company-Specific Focus Areas', fontsize=9, ha='center')
    
    ax.arrow(5, y_pos-1, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 2
    
    # Step 5: Phase Construction
    phase_title = FancyBboxPatch((1, y_pos), 8, 0.4, 
                                 boxstyle="round,pad=0.05", 
                                 edgecolor='black', facecolor='#FFF176', 
                                 linewidth=2)
    ax.add_patch(phase_title)
    ax.text(5, y_pos+0.2, 'Step 5: Roadmap Phase Construction', fontsize=12, fontweight='bold', ha='center')
    
    y_pos -= 0.6
    
    # Phase 1
    phase1_box = FancyBboxPatch((0.5, y_pos-0.5), 4, 1, 
                                boxstyle="round,pad=0.08", 
                                edgecolor='#4CAF50', facecolor='#E8F5E9', 
                                linewidth=2)
    ax.add_patch(phase1_box)
    ax.text(2.5, y_pos-0.05, 'Phase 1: Foundation', fontsize=10, fontweight='bold', ha='center')
    ax.text(2.5, y_pos-0.22, '• Core CS fundamentals', fontsize=8, ha='center')
    ax.text(2.5, y_pos-0.35, '• Basic programming', fontsize=8, ha='center')
    
    # Phase 2
    phase2_box = FancyBboxPatch((5.5, y_pos-0.5), 4, 1, 
                                boxstyle="round,pad=0.08", 
                                edgecolor='#2196F3', facecolor='#E3F2FD', 
                                linewidth=2)
    ax.add_patch(phase2_box)
    ax.text(7.5, y_pos-0.05, 'Phase 2: Core Skills', fontsize=10, fontweight='bold', ha='center')
    ax.text(7.5, y_pos-0.22, '• DSA / ML algorithms', fontsize=8, ha='center')
    ax.text(7.5, y_pos-0.35, '• System design basics', fontsize=8, ha='center')
    
    y_pos -= 1.1
    
    # Phase 3
    phase3_box = FancyBboxPatch((0.5, y_pos-0.5), 4, 1, 
                                boxstyle="round,pad=0.08", 
                                edgecolor='#FF9800', facecolor='#FFF3E0', 
                                linewidth=2)
    ax.add_patch(phase3_box)
    ax.text(2.5, y_pos-0.05, 'Phase 3: Advanced', fontsize=10, fontweight='bold', ha='center')
    ax.text(2.5, y_pos-0.22, '• Advanced patterns', fontsize=8, ha='center')
    ax.text(2.5, y_pos-0.35, '• Specialization topics', fontsize=8, ha='center')
    
    # Phase 4
    phase4_box = FancyBboxPatch((5.5, y_pos-0.5), 4, 1, 
                                boxstyle="round,pad=0.08", 
                                edgecolor='#9C27B0', facecolor='#F3E5F5', 
                                linewidth=2)
    ax.add_patch(phase4_box)
    ax.text(7.5, y_pos-0.05, 'Phase 4: Projects', fontsize=10, fontweight='bold', ha='center')
    ax.text(7.5, y_pos-0.22, '• Real-world projects', fontsize=8, ha='center')
    ax.text(7.5, y_pos-0.35, '• Portfolio building', fontsize=8, ha='center')
    
    y_pos -= 1.1
    
    # Phase 5
    phase5_box = FancyBboxPatch((2.5, y_pos-0.5), 5, 1, 
                                boxstyle="round,pad=0.08", 
                                edgecolor='#F44336', facecolor='#FFEBEE', 
                                linewidth=2)
    ax.add_patch(phase5_box)
    ax.text(5, y_pos-0.05, 'Phase 5: Interview Prep', fontsize=10, fontweight='bold', ha='center')
    ax.text(5, y_pos-0.22, '• Mock interviews • Company-specific prep', fontsize=8, ha='center')
    ax.text(5, y_pos-0.35, '• Behavioral questions • System design rounds', fontsize=8, ha='center')
    
    ax.arrow(5, y_pos-0.5, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 1.4
    
    # Step 6: Enhancement Layer
    enhance_box = FancyBboxPatch((0.5, y_pos-1), 9, 1.6, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='#7B1FA2', facecolor=ai_color, 
                                 linewidth=3)
    ax.add_patch(enhance_box)
    ax.text(5, y_pos, 'Step 6: AI Enhancement Layer', fontsize=12, fontweight='bold', ha='center')
    
    ax.text(5, y_pos-0.3, '💡 Add "Why interviewers ask this" for each topic', fontsize=9, ha='center')
    ax.text(5, y_pos-0.50, '❓ Generate common interview questions', fontsize=9, ha='center')
    ax.text(5, y_pos-0.70, '⚠️ Identify red flags to avoid', fontsize=9, ha='center')
    ax.text(5, y_pos-0.90, '📚 Suggest learning resources', fontsize=9, ha='center')
    
    ax.arrow(5, y_pos-1, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 2
    
    # Step 7: Dependency Mapping
    dependency_box = FancyBboxPatch((1.5, y_pos-0.7), 7, 1.1, 
                                    boxstyle="round,pad=0.1", 
                                    edgecolor='#5E35B1', facecolor=process_color, 
                                    linewidth=2)
    ax.add_patch(dependency_box)
    ax.text(5, y_pos, 'Step 7: Topic Dependency Resolution', fontsize=12, fontweight='bold', ha='center')
    
    ax.text(5, y_pos-0.3, 'Example: OS → System Design', fontsize=9, ha='center')
    ax.text(5, y_pos-0.5, 'Reason: Must understand processes before designing distributed systems', fontsize=8, ha='center', style='italic')
    
    ax.arrow(5, y_pos-0.7, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 1.6
    
    # Step 8: Timeline Allocation
    timeline_box = FancyBboxPatch((1, y_pos-0.6), 8, 0.9, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='#5E35B1', facecolor=process_color, 
                                  linewidth=2)
    ax.add_patch(timeline_box)
    ax.text(5, y_pos, 'Step 8: Intelligent Timeline Allocation', fontsize=12, fontweight='bold', ha='center')
    
    ax.text(5, y_pos-0.28, '⏱️ Distribute topics across user\'s timeline', fontsize=9, ha='center')
    ax.text(5, y_pos-0.45, '📅 Set realistic milestones with buffer time', fontsize=9, ha='center')
    
    ax.arrow(5, y_pos-0.6, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 1.5
    
    # Step 9: Output Generation
    output_box = FancyBboxPatch((0.5, y_pos-0.9), 9, 1.4, 
                                boxstyle="round,pad=0.1", 
                                edgecolor='#388E3C', facecolor=output_color, 
                                linewidth=3)
    ax.add_patch(output_box)
    ax.text(5, y_pos, 'Step 9: Final Roadmap Generation', fontsize=12, fontweight='bold', ha='center')
    
    ax.text(5, y_pos-0.3, '📄 Structured JSON for UI rendering', fontsize=9, ha='center')
    ax.text(5, y_pos-0.48, '📊 Visual timeline with progress tracking', fontsize=9, ha='center')
    ax.text(5, y_pos-0.66, '📋 Downloadable PDF report', fontsize=9, ha='center')
    
    ax.arrow(5, y_pos-0.9, 0, -0.3, head_width=0.15, head_length=0.1, fc='black', ec='black', linewidth=2)
    y_pos -= 1.5
    
    # Final Output
    final_box = FancyBboxPatch((1.5, y_pos-0.5), 7, 0.8, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='#2E7D32', facecolor='#A5D6A7', 
                               linewidth=3)
    ax.add_patch(final_box)
    ax.text(5, y_pos-0.05, '✅ Personalized Career Roadmap Ready!', fontsize=12, fontweight='bold', ha='center')
    ax.text(5, y_pos-0.3, 'Adaptive • Interview-Ready • Project-Driven', fontsize=9, ha='center', style='italic')
    
    # Side note
    note_box = FancyBboxPatch((0.2, 0.5), 9.6, 0.8, 
                              boxstyle="round,pad=0.05", 
                              edgecolor='#FF5722', facecolor='#FFE0B2', 
                              linewidth=2)
    ax.add_patch(note_box)
    ax.text(5, 1.1, '🔄 Continuous Adaptation: Roadmap continuously adapts based on:', fontsize=10, fontweight='bold', ha='center')
    ax.text(5, 0.85, 'User Progress • Performance in Mock Interviews • Topics Marked Difficult • Feedback from Reviewer Agent', 
            fontsize=8, ha='center')
    
    plt.tight_layout()
    plt.savefig('d:/AI Career Roadmap Generator/architecture/images/04_roadmap_generation_flow.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ Roadmap Generation Flow diagram generated successfully!")

if __name__ == "__main__":
    create_roadmap_generation_flow()
