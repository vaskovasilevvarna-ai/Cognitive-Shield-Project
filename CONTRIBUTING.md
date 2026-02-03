Contributing to Cognitive Shield 🛡️
First of all, thank you for considering contributing to the Cognitive Shield project! To maintain the project's integrity and neutrality, we follow specific guidelines for different types of contributions.

💻 For Developers: Expanding fallacies.json
The heart of our detection logic lies in the fallacy database. If you want to add a new manipulation technique or logical fallacy:

Navigate to data/fallacies.json.

Follow the existing schema: Ensure your entry includes a name, description, category (e.g., Emotional, Logical, Rhetorical), and examples.

Open a Pull Request: Briefly explain why this fallacy is essential for the "Shield" and provide a source or link to its formal definition.

🔍 For Researchers: Transparency Module Sources
We are constantly looking for reliable, open-data APIs to track media ownership and funding.

Identify a source: Look for official trade registers, NGO databases (like OpenCorporates), or government transparency portals.

Proposal: Open an Issue in this repository labeled new-source. Include the URL of the data source and a brief description of what information it provides (e.g., "Beneficial ownership for country X").

Adapter Logic: If you are technically inclined, you can propose a Python-based "adapter" to parse this specific data into our standardized format.

🌍 For Translators: Localizing the Shield
The fight against manipulation is global. We want the Shield to be accessible in every language.

Documentation: You can translate the MANIFESTO.md or CORE_PRINCIPLES.md. Please save these as FILENAME_XX.md (e.g., MANIFESTO_FR.md).

UI & Fallacies: Help us translate the descriptions in fallacies.json. We plan to move these strings into .po or .json localization files soon.

Process: Submit a Pull Request with the tag translation.

📜 Ethical Conduct
All contributors must adhere to our Core Principles:

Neutrality: Contributions must not target specific political parties or individuals, but rather the methods they use.

Openness: All code must remain under the AGPLv3 license.
