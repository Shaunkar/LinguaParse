## Multilanguage Invoice Extractor:

**Say goodbye to language barriers and manual invoice analysis!**

This project presents a powerful tool for extracting information from invoices in multiple languages using cutting-edge AI technology. Built with Streamlit and Google's Gemini Pro Vision model, it simplifies invoice processing and saves you valuable time.

**Key Features:**

* **Multilingual Support:** Understand invoices in various languages, freeing you from translation hassles.
* **AI-powered Extraction:** Leverage the power of AI to automatically extract key information like vendor, date, amount, and items.
* **Interactive Interface:** Upload an invoice image, provide an input prompt, and instantly receive comprehensive insights.
* **Flexible and Customizable:** Adapt the app to your specific needs by modifying configuration and processing steps.

**Getting Started:**

1. **Clone the repository:** `git clone https://github.com/Shaunkar/LinguaParse.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set your Google API key:** Update `config/config.py` with your API key from Google Cloud Platform.
4. **Run the app:** `streamlit run app.py`


**Technical Overview:**

The project utilizes a modular structure:

* `app.py`: Handles the Streamlit front-end and main application logic.
* `config`: Stores configuration settings like API key.
* `models`: Contains a class for interacting with the Gemini Pro Vision model.
* `utils`: Offers image processing utilities.

**Contributing:**

We welcome contributions! Feel free to fork the repository, create pull requests with enhancements or bug fixes, and join the discussions.

**Future Plans:**

* **Support for additional languages:** Expand the multilingual capabilities.
* **Advanced customization options:** Empower users to fine-tune the extraction process.
* **Integration with other tools:** Connect with accounting software or document management systems.

**Embrace the future of invoice processing with this easy-to-use and powerful tool! Start exploring now and discover how it can simplify your financial workflows.**

