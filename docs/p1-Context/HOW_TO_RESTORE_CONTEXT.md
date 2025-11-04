# HOW TO RESTORE CONTEXT IN A NEW CHAT

## 📌 Purpose
This guide explains how to restore full project context when starting a new chat
with Claude (e.g., if the current conversation becomes too long).

---

## 🎯 OPTION 1: Full Context Restoration (Recommended)

Use this when you want Claude to have complete understanding of everything.

### Step 1: Start New Chat
Open a fresh Claude chat window.

### Step 2: Paste Master Context
Copy the entire contents of **MASTER_CONTEXT.txt** and paste with this prompt:

```
I'm continuing work on the DPR Automation Platform project. 
Here is the complete context from our previous conversation. 
Please read this carefully and confirm you understand where we are.

[PASTE ENTIRE MASTER_CONTEXT.txt CONTENTS HERE]

Current Status: Completed Stage 2, ready for Stage 3
Are you ready to continue?
```

### Step 3: Wait for Confirmation
Claude will:
- Read and understand all context
- Confirm current stage
- Ask if you want to proceed

---

## ⚡ OPTION 2: Quick Context (For Simple Questions)

Use this when you just need a quick answer and don't need to continue building.

### Step 1: Start New Chat
Open a fresh Claude chat window.

### Step 2: Paste Quick Reference
Copy **QUICK_REFERENCE.txt** and paste with your question:

```
Quick context for DPR Automation Platform:

[PASTE QUICK_REFERENCE.txt CONTENTS HERE]

Question: [Your specific question]
```

---

## 📋 OPTION 3: Resuming Active Development

Use this when you're ready to continue building the next stage.

### Step 1: Start New Chat
Open a fresh Claude chat window.

### Step 2: Full Context + Files
```
I'm continuing the DPR Automation Platform project. 
Here's the complete context:

[PASTE MASTER_CONTEXT.txt]

I also have these files ready:
- config.py
- lg_utility.py  
- dpr_orchestrator.py (Stage 2 version)
- data_collection_agent.py
- dpr_main.py

Stage 2 is tested and working. Ready to proceed with Stage 3?
```

---

## 🔧 Alternative: Use Context Documents as Reference

Instead of pasting everything, you can:

1. **Upload MASTER_CONTEXT.txt** as a file attachment to Claude
2. Say: "Please read this context file and let me know when you're ready"
3. Claude will read and understand the full context

---

## 📚 What Each Document Contains

### MASTER_CONTEXT.txt (14KB)
✅ Complete project overview
✅ All architecture decisions
✅ Stage-by-stage plan
✅ Reference code patterns
✅ User requirements
✅ Current state and test results
✅ Communication style guidelines
✅ Everything needed to continue

### QUICK_REFERENCE.txt (1.4KB)
✅ Current file structure
✅ Graph flow
✅ Completed stages
✅ Next steps
✅ Key rules
✅ Quick lookup info

### README_STAGE2.md (6.7KB)
✅ Stage 2 specific documentation
✅ Setup instructions
✅ Expected output
✅ Git workflow
✅ Troubleshooting

---

## ✨ Pro Tips

1. **Save Locally:** Keep MASTER_CONTEXT.txt on your computer, update after each stage

2. **Version It:** Add to Git repo so it's always available
   ```bash
   git add MASTER_CONTEXT.txt QUICK_REFERENCE.txt
   git commit -m "Add context documents for session continuity"
   ```

3. **Update After Each Stage:** When completing a stage, update MASTER_CONTEXT.txt:
   - Mark stage as complete
   - Update "Current State" section
   - Update "Next Steps" section

4. **Use Comments:** Add your own notes to MASTER_CONTEXT.txt:
   ```
   [USER NOTE: Had issue with X, fixed by doing Y]
   ```

---

## 🎯 Example: Starting Stage 3 in New Chat

```
Hi Claude! I'm continuing the DPR Automation Platform project.

Here's the full context:
[PASTE MASTER_CONTEXT.txt]

Current Status:
- Stage 1: ✅ Complete (orchestrator foundation)
- Stage 2: ✅ Complete (data collection agent)
- Stage 3: Ready to start (financial modeling agent)

I've tested Stage 2 successfully. All data extraction and validation 
working perfectly. Ready to build the Financial Modeling Agent?

Please confirm you understand the context and we can proceed.
```

---

## ❓ FAQ

**Q: Do I need to paste the context every time?**
A: Only when starting a new chat. Within the same chat, Claude remembers everything.

**Q: Can I just say "remember our DPR project"?**
A: No, Claude doesn't have access to previous chats. You must provide the context.

**Q: What if MASTER_CONTEXT.txt is too long?**
A: Claude can handle it. The document is designed to be comprehensive but efficient.

**Q: Should I include code files?**
A: Not necessary. MASTER_CONTEXT.txt describes everything. Upload actual code 
only if Claude needs to modify specific files.

---

## 📝 Summary

**For New Chat:**
1. Copy MASTER_CONTEXT.txt
2. Paste in new chat with "I'm continuing this project..."
3. Claude confirms understanding
4. Continue where you left off

**Simple!** 🎯

---

**Created:** October 27, 2025
**Version:** 1.0
**Project:** DPR Automation Platform