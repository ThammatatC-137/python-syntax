"""
Given a flow chart below 
(simplified from: https://www.radcliffecardiology.com/image-gallery/figure-1-flow-chart-suggested-strategies-coronary-artery-disease-management), 
write a program to suggest the Transcatheter Aortic Valve Implantation (TAVI) management strategy 
for Coronary Artery Disease (CAD).

Logic:
1. First check if CAD is obstructive
2. If non-obstructive → TAVI alone
3. If obstructive → check area of myocardium at risk
4. If small area → TAVI first, then ischemia-driven revascularization  
5. If large area → check coronary stenosis percentage
   - If > 75% → Severe CAD → Staged upfront or concomitant PCI and TAVI
   - If ≤ 75% → Moderate CAD → TAVI first, then CAD functional assessment
"""


obstructive = input('Is CAD obstructive (yes/no)? ').lower().strip()

if obstructive == 'no':
    # Non-obstructive CAD path
    print('Non-obstructive CAD.')
    print('TAVI alone.')
elif obstructive == 'yes':
    # Obstructive CAD path
    print('Obstructive CAD.')
    
    # Check area of myocardium at risk
    risk_area = input('Is area of myocardium at risk large (yes/no)? ').lower().strip()
    
    if risk_area == 'no':
        # Small area of myocardium at risk
        print('Small area of myocardium at risk.')
        print('Consider TAVI first, then ischemia-driven revascularization.')
    elif risk_area == 'yes':
        # Large area of myocardium at risk
        print('Large area of myocardium at risk.')
        
        # Check coronary stenosis percentage
        while True:
            try:
                CS = float(input('How is coronary stenosis (%)? '))
                break  # Exit loop if conversion successful
            except ValueError:
                print('Please enter a valid percentage number (e.g., 60, 80.5).')
        
        if CS > 75:
            # Severe CAD (coronary stenosis > 75%)
            print('Severe CAD.')
            print('Staged upfront or concomitant PCI and TAVI.')
        else:
            # Moderate CAD (coronary stenosis ≤ 75%)
            print('Moderate CAD.')
            print('Consider TAVI first, then CAD functional assessment.')
    else:
        print('Invalid input. Please enter yes or no.')
else:
    print('Invalid input. Please enter yes or no.')


