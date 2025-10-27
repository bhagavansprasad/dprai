"""
AI prompt templates for DPR generation
All prompts for Gemini AI are defined here
"""


def get_executive_summary_prompt(user_input: dict) -> str:
    """
    Generate prompt for Executive Summary section
    
    Args:
        user_input: Dictionary containing user input data
        
    Returns:
        Formatted prompt string for Gemini
    """
    
    products_list = ", ".join(user_input.get("products", []))
    
    prompt = f"""
You are an expert consultant specializing in MSME cluster development and Detailed Project Reports (DPRs) for the Government of India's MSE-CDP scheme.

Generate a compelling and professional Executive Summary for a Detailed Project Report (DPR) for establishing a Common Facility Centre (CFC).

**CLUSTER DETAILS:**
- Cluster Name: {user_input.get('cluster_name')}
- Industry: {user_input.get('industry')}
- Location: {user_input.get('city')}, {user_input.get('district')}, {user_input.get('state')}
- Number of Units: {user_input.get('num_units')} (Micro: {user_input.get('num_micro')}, Small: {user_input.get('num_small')}, Medium: {user_input.get('num_medium')})
- Current Annual Turnover: ₹{user_input.get('current_turnover')} Crores
- Employment: {user_input.get('direct_employment')} direct, {user_input.get('indirect_employment')} indirect
- Products/Services: {products_list}
- Cluster Age: {user_input.get('cluster_age')} years

**STRUCTURE REQUIREMENTS:**
The Executive Summary must include these sections in order:

1. **Introduction** (1 paragraph)
   - Introduce the cluster and its role in the regional economy
   - Mention the industry significance and contribution to MSME sector

2. **Current State and Significance** (1 paragraph)
   - Current operational status (units, turnover, employment)
   - Market presence and products/services offered
   - Strategic importance to the region

3. **Challenges and Problems** (1 paragraph)
   - Key challenges faced by cluster units
   - Technology gaps and infrastructure limitations
   - Impact on competitiveness and growth

4. **Proposed CFC Intervention** (1 paragraph)
   - Overview of the proposed Common Facility Centre
   - Key facilities and equipment to be provided
   - How CFC will address identified problems

5. **Expected Outcomes and Impact** (1 paragraph)
   - Projected improvements in productivity and quality
   - Expected increase in turnover and employment
   - Market expansion opportunities
   - Long-term sustainability and growth vision

**WRITING GUIDELINES:**
- Length: 400-500 words total
- Tone: Professional, persuasive, data-driven
- Audience: Government officials, financial institutions, policy makers
- Style: Clear, concise, compelling
- Use specific numbers and data points
- Avoid jargon; use accessible language
- Focus on impact and transformation

**OUTPUT:**
Generate ONLY the executive summary text. Do not include any meta-commentary, explanations, or additional notes.
"""
    
    return prompt


def get_cluster_profile_prompt(user_input: dict) -> str:
    """
    Generate prompt for Cluster Profile section
    
    Args:
        user_input: Dictionary containing user input data
        
    Returns:
        Formatted prompt string for Gemini
    """
    
    products_list = ", ".join(user_input.get("products", []))
    
    prompt = f"""
You are an expert consultant specializing in MSME cluster development and Detailed Project Reports (DPRs).

Generate a comprehensive and detailed Cluster Profile section for a Detailed Project Report (DPR).

**CLUSTER INFORMATION:**
- Cluster Name: {user_input.get('cluster_name')}
- Industry: {user_input.get('industry')}
- Location: {user_input.get('city')}, {user_input.get('district')}, {user_input.get('state')}
- Age of Cluster: {user_input.get('cluster_age')} years
- Total Units: {user_input.get('num_units')}
  - Micro Units: {user_input.get('num_micro')}
  - Small Units: {user_input.get('num_small')}
  - Medium Units: {user_input.get('num_medium')}
- Current Turnover: ₹{user_input.get('current_turnover')} Crores
- Employment:
  - Direct: {user_input.get('direct_employment')}
  - Indirect: {user_input.get('indirect_employment')}
- Products/Services: {products_list}

**SECTIONS TO COVER:**

1. **History and Development of the Cluster**
   - Origins and evolution over {user_input.get('cluster_age')} years
   - Key milestones in cluster development
   - Growth trajectory and expansion

2. **Geographic Spread and Location Advantages**
   - Physical location and area covered
   - Proximity to markets, raw materials, transportation
   - Strategic advantages of the location
   - Infrastructure availability (roads, power, water)

3. **Nature and Type of Units**
   - Breakdown of micro, small, and medium enterprises
   - Ownership patterns (family-owned, partnerships, etc.)
   - Scale of operations and investment levels
   - Mix of formal and informal units

4. **Products and Services Portfolio**
   - Detailed description of main products/services
   - Product categories and variants
   - Quality standards and certifications
   - Unique selling propositions

5. **Current Technology and Processes**
   - Technology currently used by cluster units
   - Production processes and methods
   - Level of automation and mechanization
   - Equipment and machinery commonly used

6. **Employment Generation and Workforce**
   - Direct and indirect employment breakdown
   - Skill levels and expertise available
   - Gender distribution (if relevant)
   - Training and skill development initiatives

7. **Market Reach and Customer Base**
   - Primary markets (local/regional/national/export)
   - Key customer segments
   - Market share and competition
   - Distribution channels

8. **Unique Characteristics and Strengths**
   - What makes this cluster distinctive
   - Core competencies and specializations
   - Cluster's reputation in the market
   - Collaborative practices among units

**WRITING GUIDELINES:**
- Length: 600-800 words total
- Tone: Descriptive, factual, professional
- Style: Clear, informative, well-structured
- Use specific data points and examples
- Maintain objectivity while highlighting strengths
- Write in third person
- Use industry-appropriate terminology

**OUTPUT:**
Generate ONLY the cluster profile text. Do not include headings, titles, or meta-commentary.
Write as a continuous narrative with clear paragraph breaks between sections.
"""
    
    return prompt