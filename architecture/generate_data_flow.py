"""
Generate Data Flow Diagram for AI Career Roadmap Generator
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def create_data_flow_diagram():
    fig, ax = plt.subplots(figsize=(16, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(5, 11.5, 'Data Flow Diagram - Information Movement', 
            fontsize=20, fontweight='bold', ha='center')
    
    # Colors
    user_color = '#FFCDD2'
    data_color = '#B3E5FC'
    process_color = '#C5E1A5'
    storage_color = '#F0F4C3'
    
    # External Entity: User
    user_box = FancyBboxPatch((0.5, 10), 1.5, 0.8, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='#D32F2F', facecolor=user_color, 
                              linewidth=3)
    ax.add_patch(user_box)
    ax.text(1.25, 10.4, '👤 User', fontsize=12, fontweight='bold', ha='center')
    
    # Process 1: User Registration/Login
    process1 = mpatches.Circle((3.5, 10.4), 0.5, color=process_color, ec='black', linewidth=2)
    ax.add_patch(process1)
    ax.text(3.5, 10.4, 'P1', fontsize=10, fontweight='bold', ha='center')
    ax.text(3.5, 9.5, 'Auth\nProcess', fontsize=9, ha='center')
    
    # Arrow: User to Process 1
    arrow1 = FancyArrowPatch((2, 10.4), (3, 10.4),
                             arrowstyle='->', mutation_scale=20, 
                             linewidth=2, color='#424242')
    ax.add_patch(arrow1)
    ax.text(2.5, 10.6, 'Login/Signup', fontsize=8, ha='center')
    
    # Data Store 1: User Database
    db1 = FancyBboxPatch((5.5, 10), 2, 0.8, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#827717', facecolor=storage_color, 
                         linewidth=2)
    ax.add_patch(db1)
    ax.text(6.5, 10.4, 'D1: User DB', fontsize=10, fontweight='bold', ha='center')
    ax.text(6.5, 10.15, 'Auth & Profile', fontsize=8, ha='center')
    
    # Arrow: Process 1 to DB1
    arrow2 = FancyArrowPatch((4, 10.4), (5.5, 10.4),
                             arrowstyle='<->', mutation_scale=20, 
                             linewidth=2, color='#424242')
    ax.add_patch(arrow2)
    ax.text(4.75, 10.6, 'Store/Retrieve', fontsize=8, ha='center')
    
    # Process 2: Profile Creation
    process2 = mpatches.Circle((1.25, 8.5), 0.5, color=process_color, ec='black', linewidth=2)
    ax.add_patch(process2)
    ax.text(1.25, 8.5, 'P2', fontsize=10, fontweight='bold', ha='center')
    ax.text(1.25, 7.6, 'Profile\nCreation', fontsize=9, ha='center')
    
    # Arrow: User to Process 2
    arrow3 = FancyArrowPatch((1.25, 10), (1.25, 9),
                             arrowstyle='->', mutation_scale=20, 
                             linewidth=2, color='#424242')
    ax.add_patch(arrow3)
    ax.text(0.7, 9.5, 'Profile Data', fontsize=8, ha='center', rotation=90)
    
    # Data: Profile Information
    data1 = FancyBboxPatch((2.3, 8.2), 2.2, 0.6, 
                           boxstyle="round,pad=0.05", 
                           edgecolor='#0277BD', facecolor=data_color, 
                           linewidth=1.5, linestyle='--')
    ax.add_patch(data1)
    ax.text(3.4, 8.5, 'Skills, Experience,', fontsize=8, ha='center')
    ax.text(3.4, 8.3, 'Target Role, Timeline', fontsize=8, ha='center')
    
    # Arrow: Process 2 to Data1
    arrow4 = FancyArrowPatch((1.75, 8.5), (2.3, 8.5),
                             arrowstyle='->', mutation_scale=15, 
                             linewidth=1.5, color='#424242')
    ax.add_patch(arrow4)
    
    # Process 3: AI Analysis
    process3 = mpatches.Circle((6, 8.5), 0.5, color=process_color, ec='black', linewidth=2)
    ax.add_patch(process3)
    ax.text(6, 8.5, 'P3', fontsize=10, fontweight='bold', ha='center')
    ax.text(6, 7.6, 'AI Profile\nAnalysis', fontsize=9, ha='center')
    
    # Arrow: Data1 to Process 3
    arrow5 = FancyArrowPatch((4.5, 8.5), (5.5, 8.5),
                             arrowstyle='->', mutation_scale=20, 
                             linewidth=2, color='#424242')
    ax.add_patch(arrow5)
    
    # Arrow: Process 3 to DB1
    arrow6 = FancyArrowPatch((6.3, 8.9), (6.5, 10),
                             arrowstyle='<->', mutation_scale=20, 
                             linewidth=2, color='#424242')
    ax.add_patch(arrow6)
    ax.text(6.8, 9.4, 'Save\nProfile', fontsize=8, ha='center')
    
    # Process 4: Roadmap Generation
    process4 = mpatches.Circle((3.5, 6.5), 0.6, color='#BA68C8', ec='black', linewidth=3)
    ax.add_patch(process4)
    ax.text(3.5, 6.5, 'P4', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(3.5, 5.4, 'AI Roadmap\nGenerator', fontsize=10, ha='center', fontweight='bold')
    
    # Arrow: Process 3 to Process 4
    arrow7 = FancyArrowPatch((6, 8), (4, 7),
                             arrowstyle='->', mutation_scale=20, 
                             linewidth=2.5, color='#7B1FA2')
    ax.add_patch(arrow7)
    ax.text(5.3, 7.6, 'Analyzed\nProfile', fontsize=8, ha='center')
    
    # Data Store 2: Knowledge Base
    db2 = FancyBboxPatch((0.3, 5.9), 2, 1.2, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#827717', facecolor=storage_color, 
                         linewidth=2)
    ax.add_patch(db2)
    ax.text(1.3, 6.8, 'D2: Knowledge', fontsize=10, fontweight='bold', ha='center')
    ax.text(1.3, 6.55, 'Base', fontsize=10, fontweight='bold', ha='center')
    ax.text(1.3, 6.3, '• Interview Q&A', fontsize=7, ha='center')
    ax.text(1.3, 6.1, '• Topic Templates', fontsize=7, ha='center')
    
    # Arrow: DB2 to Process 4
    arrow8 = FancyArrowPatch((2.3, 6.5), (2.9, 6.5),
                             arrowstyle='->', mutation_scale=20, 
                             linewidth=2, color='#424242')
    ax.add_patch(arrow8)
    ax.text(2.6, 6.75, 'Templates', fontsize=7, ha='center')
    
    # Data Store 3: Roadmap Database
    db3 = FancyBboxPatch((5.5, 5.9), 2, 1.2, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#827717', facecolor=storage_color, 
                         linewidth=2)
    ax.add_patch(db3)
    ax.text(6.5, 6.8, 'D3: Roadmap', fontsize=10, fontweight='bold', ha='center')
    ax.text(6.5, 6.55, 'Store', fontsize=10, fontweight='bold', ha='center')
    ax.text(6.5, 6.3, '• Generated paths', fontsize=7, ha='center')
    ax.text(6.5, 6.1, '• User progress', fontsize=7, ha='center')
    
    # Arrow: Process 4 to DB3
    arrow9 = FancyArrowPatch((4.1, 6.5), (5.5, 6.5),
                             arrowstyle='->', mutation_scale=20, 
                             linewidth=2.5, color='#7B1FA2')
    ax.add_patch(arrow9)
    ax.text(4.8, 6.75, 'Save\nRoadmap', fontsize=8, ha='center')
    
    # Process 5: Display Roadmap
    process5 = mpatches.Circle((8.5, 6.5), 0.5, color=process_color, ec='black', linewidth=2)
    ax.add_patch(process5)
    ax.text(8.5, 6.5, 'P5', fontsize=10, fontweight='bold', ha='center')
    ax.text(8.5, 5.6, 'Render\nDashboard', fontsize=9, ha='center')
    
    # Arrow: DB3 to Process 5
    arrow10 = FancyArrowPatch((7.5, 6.5), (8, 6.5),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2, color='#424242')
    ax.add_patch(arrow10)
    
    # Arrow: Process 5 to User
    arrow11 = FancyArrowPatch((8.5, 7), (1.25, 9.8),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2, color='#D32F2F', linestyle='--')
    ax.add_patch(arrow11)
    ax.text(5.5, 8.7, 'Display Roadmap', fontsize=9, ha='center', color='#D32F2F')
    
    # Process 6: Learning Activity
    process6 = mpatches.Circle((1.5, 4), 0.5, color=process_color, ec='black', linewidth=2)
    ax.add_patch(process6)
    ax.text(1.5, 4, 'P6', fontsize=10, fontweight='bold', ha='center')
    ax.text(1.5, 3.1, 'Learning\nSession', fontsize=9, ha='center')
    
    # Arrow: User to Process 6
    arrow12 = FancyArrowPatch((1.25, 10), (1.5, 4.5),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=1.5, color='#424242', linestyle=':')
    ax.add_patch(arrow12)
    ax.text(0.5, 7, 'Start\nLearning', fontsize=8, ha='center', rotation=80)
    
    # Process 7: AI Mentor
    process7 = mpatches.Circle((4, 4), 0.5, color='#BA68C8', ec='black', linewidth=2)
    ax.add_patch(process7)
    ax.text(4, 4, 'P7', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(4, 3.1, 'AI Mentor\nAgent', fontsize=9, ha='center')
    
    # Arrow: Process 6 to Process 7
    arrow13 = FancyArrowPatch((2, 4), (3.5, 4),
                              arrowstyle='<->', mutation_scale=20, 
                              linewidth=2, color='#7B1FA2')
    ax.add_patch(arrow13)
    ax.text(2.75, 4.25, 'Q&A', fontsize=8, ha='center')
    
    # Process 8: Mock Interview
    process8 = mpatches.Circle((6.5, 4), 0.5, color='#BA68C8', ec='black', linewidth=2)
    ax.add_patch(process8)
    ax.text(6.5, 4, 'P8', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(6.5, 3.1, 'Interviewer\nAgent', fontsize=9, ha='center')
    
    # Arrow: User to Process 8
    arrow14 = FancyArrowPatch((1.25, 10), (6.5, 4.5),
                              arrowstyle='<->', mutation_scale=20, 
                              linewidth=1.5, color='#424242', linestyle=':')
    ax.add_patch(arrow14)
    ax.text(3.5, 7.5, 'Practice', fontsize=8, ha='center', rotation=-55)
    
    # Data Store 4: Vector DB
    db4 = FancyBboxPatch((8, 3.5), 1.8, 1, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#827717', facecolor=storage_color, 
                         linewidth=2)
    ax.add_patch(db4)
    ax.text(8.9, 4.2, 'D4: Vector DB', fontsize=9, fontweight='bold', ha='center')
    ax.text(8.9, 3.95, 'Q&A Embeddings', fontsize=7, ha='center')
    ax.text(8.9, 3.75, 'Interview Bank', fontsize=7, ha='center')
    
    # Arrow: DB4 to Process 7 and 8
    arrow15 = FancyArrowPatch((8, 4), (4.5, 4),
                              arrowstyle='->', mutation_scale=15, 
                              linewidth=1.5, color='#424242')
    ax.add_patch(arrow15)
    
    arrow16 = FancyArrowPatch((8, 4), (7, 4),
                              arrowstyle='->', mutation_scale=15, 
                              linewidth=1.5, color='#424242')
    ax.add_patch(arrow16)
    
    # Process 9: Progress Update
    process9 = mpatches.Circle((3.5, 2), 0.5, color=process_color, ec='black', linewidth=2)
    ax.add_patch(process9)
    ax.text(3.5, 2, 'P9', fontsize=10, fontweight='bold', ha='center')
    ax.text(3.5, 1.1, 'Update\nProgress', fontsize=9, ha='center')
    
    # Arrow: Process 6 to Process 9
    arrow17 = FancyArrowPatch((1.5, 3.5), (3.2, 2.3),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2, color='#424242')
    ax.add_patch(arrow17)
    ax.text(2, 2.7, 'Completed', fontsize=8, ha='center')
    
    # Arrow: Process 9 to DB3
    arrow18 = FancyArrowPatch((4, 2.3), (6, 5.9),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2, color='#424242')
    ax.add_patch(arrow18)
    ax.text(5.3, 4, 'Save\nProgress', fontsize=8, ha='center')
    
    # Process 10: Adaptive Engine
    process10 = mpatches.Circle((6.5, 2), 0.6, color='#BA68C8', ec='black', linewidth=3)
    ax.add_patch(process10)
    ax.text(6.5, 2, 'P10', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(6.5, 0.9, 'AI Reviewer\n& Adapter', fontsize=9, ha='center', fontweight='bold')
    
    # Arrow: Process 8 to Process 10
    arrow19 = FancyArrowPatch((6.5, 3.5), (6.5, 2.6),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2, color='#7B1FA2')
    ax.add_patch(arrow19)
    ax.text(6.9, 3, 'Interview\nResults', fontsize=8, ha='center')
    
    # Arrow: Process 10 to DB3 (feedback loop)
    arrow20 = FancyArrowPatch((6.5, 2.6), (6.5, 5.9),
                              arrowstyle='->', mutation_scale=20, 
                              linewidth=2.5, color='#E91E63', linestyle='--')
    ax.add_patch(arrow20)
    ax.text(7.2, 4.2, 'Adapt\nRoadmap', fontsize=9, ha='center', fontweight='bold', color='#E91E63')
    
    # Data Store 5: Cache
    db5 = FancyBboxPatch((8.5, 1.5), 1.3, 1, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#827717', facecolor=storage_color, 
                         linewidth=2)
    ax.add_patch(db5)
    ax.text(9.15, 2.2, 'D5: Cache', fontsize=9, fontweight='bold', ha='center')
    ax.text(9.15, 1.95, 'Redis', fontsize=7, ha='center')
    ax.text(9.15, 1.75, 'Sessions', fontsize=7, ha='center')
    
    # Arrow: Process 10 to DB5
    arrow21 = FancyArrowPatch((7.1, 2), (8.5, 2),
                              arrowstyle='<->', mutation_scale=15, 
                              linewidth=1.5, color='#424242')
    ax.add_patch(arrow21)
    
    # Legend
    legend_elements = [
        mpatches.Patch(color=process_color, label='Process'),
        mpatches.Patch(color='#BA68C8', label='AI Process'),
        mpatches.Patch(color=storage_color, label='Data Store'),
        mpatches.Patch(color=data_color, label='Data Flow'),
        mpatches.Patch(color=user_color, label='External Entity'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9, ncol=5)
    
    # Note
    note_text = ('Key: Solid lines = Primary data flow  |  Dashed lines = Return/Display flow  |  '
                 'Dotted lines = User interaction')
    ax.text(5, 0.3, note_text, fontsize=8, ha='center', style='italic',
            bbox=dict(boxstyle='round', facecolor='#FFF9C4', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('d:/AI Career Roadmap Generator/architecture/images/05_data_flow_diagram.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✅ Data Flow Diagram generated successfully!")

if __name__ == "__main__":
    create_data_flow_diagram()
