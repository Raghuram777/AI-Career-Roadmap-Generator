"""
Generate User Journey Flowchart for AI Career Roadmap Generator
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

def create_user_journey():
    fig, ax = plt.subplots(figsize=(14, 16))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 18)
    ax.axis('off')
    
    # Title
    ax.text(5, 17.3, 'User Journey - AI Career Roadmap Generator', 
            fontsize=20, fontweight='bold', ha='center')
    
    # Colors
    start_color = '#4CAF50'
    process_color = '#2196F3'
    decision_color = '#FF9800'
    ai_color = '#9C27B0'
    end_color = '#F44336'
    
    y_pos = 16.5
    
    # 1. Start
    start_circle = Circle((5, y_pos), 0.3, color=start_color, ec='black', linewidth=2)
    ax.add_patch(start_circle)
    ax.text(5, y_pos, 'START', fontsize=9, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7, y_pos, 'User opens app', fontsize=9, style='italic')
    
    # Arrow down
    ax.arrow(5, y_pos-0.3, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    y_pos -= 1.2
    
    # 2. Authentication
    auth_box = FancyBboxPatch((3.5, y_pos-0.4), 3, 0.8, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='black', facecolor=process_color, 
                              linewidth=2)
    ax.add_patch(auth_box)
    ax.text(5, y_pos, 'Login / Sign Up', fontsize=11, fontweight='bold', ha='center', color='white')
    
    ax.arrow(5, y_pos-0.4, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    y_pos -= 1.3
    
    # 3. Check Profile
    decision_box = mpatches.FancyBboxPatch((3.8, y_pos-0.35), 2.4, 0.7,
                                           boxstyle="round,pad=0.05",
                                           edgecolor='black', facecolor=decision_color,
                                           linewidth=2)
    ax.add_patch(decision_box)
    ax.text(5, y_pos, 'Profile Exists?', fontsize=10, fontweight='bold', ha='center')
    
    # No - Create Profile
    ax.arrow(6.2, y_pos, 0.8, 0, head_width=0.15, head_length=0.1, fc='black', ec='black')
    ax.text(7.5, y_pos+0.1, 'NO', fontsize=9, fontweight='bold')
    
    profile_box = FancyBboxPatch((7.3, y_pos-0.35), 2, 0.7, 
                                 boxstyle="round,pad=0.05", 
                                 edgecolor='black', facecolor=ai_color, 
                                 linewidth=2)
    ax.add_patch(profile_box)
    ax.text(8.3, y_pos, 'AI Onboarding', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(8.3, y_pos-0.18, '(Diagnostic Q&A)', fontsize=8, ha='center', color='white')
    
    # Arrow back down
    ax.arrow(8.3, y_pos-0.35, 0, -0.4, head_width=0.15, head_length=0.1, fc='black', ec='black')
    ax.plot([8.3, 8.3, 5, 5], [y_pos-0.75, y_pos-1.2, y_pos-1.2, y_pos-1.3], 
            'k-', linewidth=2)
    ax.arrow(5, y_pos-1.3, 0, -0.1, head_width=0.15, head_length=0.1, fc='black', ec='black')
    
    # Yes - Continue
    ax.arrow(5, y_pos-0.35, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    ax.text(5.3, y_pos-0.5, 'YES', fontsize=9, fontweight='bold')
    y_pos -= 1.8
    
    # 4. AI Profile Analysis
    analysis_box = FancyBboxPatch((3, y_pos-0.5), 4, 1, 
                                  boxstyle="round,pad=0.1", 
                                  edgecolor='black', facecolor=ai_color, 
                                  linewidth=2)
    ax.add_patch(analysis_box)
    ax.text(5, y_pos-0.05, '🤖 AI Profile Analysis', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5, y_pos-0.25, '• Skill Level Assessment', fontsize=8, ha='center', color='white')
    ax.text(5, y_pos-0.38, '• Target Role Identification', fontsize=8, ha='center', color='white')
    
    ax.arrow(5, y_pos-0.5, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    y_pos -= 1.5
    
    # 5. Generate Roadmap
    roadmap_box = FancyBboxPatch((2.5, y_pos-0.6), 5, 1.2, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='black', facecolor=ai_color, 
                                 linewidth=3)
    ax.add_patch(roadmap_box)
    ax.text(5, y_pos, '⭐ AI Roadmap Generation', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(5, y_pos-0.2, '• Role-specific learning path', fontsize=8, ha='center', color='white')
    ax.text(5, y_pos-0.33, '• Interview-aware topics', fontsize=8, ha='center', color='white')
    ax.text(5, y_pos-0.46, '• Project suggestions', fontsize=8, ha='center', color='white')
    
    ax.arrow(5, y_pos-0.6, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    y_pos -= 1.6
    
    # 6. Display Roadmap
    display_box = FancyBboxPatch((3.2, y_pos-0.5), 3.6, 1, 
                                 boxstyle="round,pad=0.1", 
                                 edgecolor='black', facecolor=process_color, 
                                 linewidth=2)
    ax.add_patch(display_box)
    ax.text(5, y_pos-0.05, '📊 View Roadmap Dashboard', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5, y_pos-0.23, '• Timeline visualization', fontsize=8, ha='center', color='white')
    ax.text(5, y_pos-0.35, '• Milestone tracking', fontsize=8, ha='center', color='white')
    
    ax.arrow(5, y_pos-0.5, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    y_pos -= 1.5
    
    # 7. Learning Loop
    learning_decision = mpatches.FancyBboxPatch((3.5, y_pos-0.4), 3, 0.8,
                                                boxstyle="round,pad=0.05",
                                                edgecolor='black', facecolor=decision_color,
                                                linewidth=2)
    ax.add_patch(learning_decision)
    ax.text(5, y_pos-0.05, 'User Action?', fontsize=11, fontweight='bold', ha='center')
    
    # Branch 1: Learn Topic
    ax.arrow(3.5, y_pos, -1, 0, head_width=0.15, head_length=0.1, fc='black', ec='black')
    ax.text(2.2, y_pos+0.15, 'Learn', fontsize=9, fontweight='bold')
    
    learn_box = FancyBboxPatch((0.5, y_pos-0.35), 1.8, 0.7, 
                               boxstyle="round,pad=0.05", 
                               edgecolor='black', facecolor=ai_color, 
                               linewidth=2)
    ax.add_patch(learn_box)
    ax.text(1.4, y_pos, '💡 AI Mentor', fontsize=9, fontweight='bold', ha='center', color='white')
    ax.text(1.4, y_pos-0.18, 'Explains topic', fontsize=7, ha='center', color='white')
    
    # Branch 2: Practice
    ax.arrow(6.5, y_pos, 1, 0, head_width=0.15, head_length=0.1, fc='black', ec='black')
    ax.text(7.8, y_pos+0.15, 'Practice', fontsize=9, fontweight='bold')
    
    practice_box = FancyBboxPatch((7.7, y_pos-0.35), 1.8, 0.7, 
                                  boxstyle="round,pad=0.05", 
                                  edgecolor='black', facecolor=ai_color, 
                                  linewidth=2)
    ax.add_patch(practice_box)
    ax.text(8.6, y_pos, '🎯 Mock Interview', fontsize=9, fontweight='bold', ha='center', color='white')
    ax.text(8.6, y_pos-0.18, 'AI questions', fontsize=7, ha='center', color='white')
    
    # Arrows back to center
    ax.plot([1.4, 1.4, 5], [y_pos-0.35, y_pos-1, y_pos-1], 'k-', linewidth=2)
    ax.plot([8.6, 8.6, 5], [y_pos-0.35, y_pos-1, y_pos-1], 'k-', linewidth=2)
    
    ax.arrow(5, y_pos-0.4, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    ax.text(5.3, y_pos-0.6, 'Complete', fontsize=9, fontweight='bold')
    
    y_pos -= 1.6
    
    # 8. Mark Progress
    progress_box = FancyBboxPatch((3.2, y_pos-0.4), 3.6, 0.8, 
                                  boxstyle="round,pad=0.05", 
                                  edgecolor='black', facecolor=process_color, 
                                  linewidth=2)
    ax.add_patch(progress_box)
    ax.text(5, y_pos, '✅ Update Progress', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(5, y_pos-0.2, 'Mark completed / Rate difficulty', fontsize=8, ha='center', color='white')
    
    ax.arrow(5, y_pos-0.4, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    y_pos -= 1.3
    
    # 9. AI Adaptation
    adapt_box = FancyBboxPatch((2.8, y_pos-0.5), 4.4, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='black', facecolor=ai_color, 
                               linewidth=3)
    ax.add_patch(adapt_box)
    ax.text(5, y_pos-0.05, '🔄 AI Adaptive Engine', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5, y_pos-0.23, '• Analyze performance', fontsize=8, ha='center', color='white')
    ax.text(5, y_pos-0.35, '• Adjust roadmap difficulty', fontsize=8, ha='center', color='white')
    
    ax.arrow(5, y_pos-0.5, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    y_pos -= 1.4
    
    # 10. Continue Decision
    continue_decision = mpatches.FancyBboxPatch((3.5, y_pos-0.35), 3, 0.7,
                                                boxstyle="round,pad=0.05",
                                                edgecolor='black', facecolor=decision_color,
                                                linewidth=2)
    ax.add_patch(continue_decision)
    ax.text(5, y_pos, 'Roadmap Complete?', fontsize=10, fontweight='bold', ha='center')
    
    # No - Loop back
    ax.plot([6.5, 8, 8, 5], [y_pos, y_pos, y_pos+8.5, y_pos+8.5], 'k--', linewidth=2)
    ax.arrow(5, y_pos+8.5, 0, -0.1, head_width=0.15, head_length=0.1, fc='black', ec='black')
    ax.text(8.3, y_pos+4, 'NO', fontsize=9, fontweight='bold')
    ax.text(8.3, y_pos+3.7, 'Continue', fontsize=8)
    ax.text(8.3, y_pos+3.5, 'Learning', fontsize=8)
    
    # Yes - Continue to completion
    ax.arrow(5, y_pos-0.35, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    ax.text(5.3, y_pos-0.5, 'YES', fontsize=9, fontweight='bold')
    y_pos -= 1.3
    
    # 11. Final Assessment
    final_box = FancyBboxPatch((3, y_pos-0.5), 4, 1, 
                               boxstyle="round,pad=0.1", 
                               edgecolor='black', facecolor=ai_color, 
                               linewidth=2)
    ax.add_patch(final_box)
    ax.text(5, y_pos-0.05, '🎓 Final Interview Simulation', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5, y_pos-0.25, '• Full mock interview', fontsize=8, ha='center', color='white')
    ax.text(5, y_pos-0.38, '• Comprehensive evaluation', fontsize=8, ha='center', color='white')
    
    ax.arrow(5, y_pos-0.5, 0, -0.5, head_width=0.15, head_length=0.1, fc='black', ec='black')
    y_pos -= 1.4
    
    # 12. End
    end_circle = Circle((5, y_pos), 0.3, color=end_color, ec='black', linewidth=2)
    ax.add_patch(end_circle)
    ax.text(5, y_pos, 'READY', fontsize=8, fontweight='bold', ha='center', va='center', color='white')
    ax.text(7, y_pos, 'Interview Ready! 🎉', fontsize=10, fontweight='bold', style='italic')
    
    # Legend
    legend_elements = [
        mpatches.Patch(color=process_color, label='User Action'),
        mpatches.Patch(color=ai_color, label='AI-Powered'),
        mpatches.Patch(color=decision_color, label='Decision Point'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('d:/AI Career Roadmap Generator/architecture/images/02_user_journey.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ User Journey flowchart generated successfully!")

if __name__ == "__main__":
    create_user_journey()
