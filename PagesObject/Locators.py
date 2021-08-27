# here the locators of all pages are declared
class Locators:

    # Text Fields
    userText = "UserId"
    passwordText = "Password"
    midText = "MerchantId"

    amountText = "Amount"
    customerIdText = "CustomerId"
    emailText = "Email"
    invoiceText = "Invoice"
    invoiceRefundText = "InvoiceNumber"
    referenceNumberRefundText = "ReferenceNumber"

    cashOpsText = "open"

    cashAmountText = "cash"

    customerCodeFormText = "customerCodeInput"
    amountCardFormText = "amountInput"
    cardNumberCardFormText = "cardNumberInput"
    monthSelect = "month"
    yearSelect = "year"
    cardNameCardFormText = "cardNameInput"
    cvvCardFormText = "cvvInput"
    invoiceCardFormText = "invoiceInput"
    emailCardFormText = "emailInput"
    addressCardFormText = "addressInput"
    zipCardFormText = "zipInput"

    clientIDCardTokenText = "customerCodeRecrringSaleInput"
    tokenCardText = "tokenCardInput"

    transactionTypeCheck = "selectTransType"
    clientIDText = "clientID"
    abaText = "aba"
    accountNumberText = "account"
    checkNumberText = "checknumber"
    checkAmountText = "amount"
    dateIssuedText = "dateissued"
    invoiceNumberText = "invoice"
    checkIdTypeSelect = "idType"
    idNumberText = "idnumber"
    statesSelect = "SelectState"
    bussinesPhoneText = "bussinesPhone"
    loanNumberText = "loanNumber"

    clientIDCheckTokenText = "cuastomerCodeRecurringCheckInput"
    tokenCheckTokenText = "tokenCheckCardInput"

    # Buttons
    logMeInButton = "button[type='submit']"
    closeButton = "body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > " \
                  "div.MuiDialogActions-root.MuiDialogActions-spacing > button"
    okButton = "okAlert"
    linkButton = "LINK"
    yesButton = "Yes"
    noButton = "No"
    doneButton = "DONE"

    addCardButton = "AddCard"
    deleteCardButton = "DeleteCard"

    addTokenCardButton = "AddTokenCard"
    deleteTokenCardButton = "DeleteTokenCard"

    addCheckButton = "AddCheck"
    deleteCheckButton = "DeleteCheck"

    addTokenCheckButton = "AddTokenCheck"
    deleteTokenCheckButton = "DeleteTokenCheck"

    addSimpleCheckButton = "AddSimpleCheck"
    deleteSimpleCheckButton = "DeleteSimpleCheck"

    addCheckConversionButton = "AddCheckConversion"
    deleteCheckConversionButton = "DeleteCheckConversion"

    addDigniFiButton = "AddDignifi"
    deleteDigniFiButton = "DeleteDignifi"

    searchTokenCardButton = "customerCodeRecurringSaleButton"

    submitCardFormButton = "submitCard"
    submitTokenCardButton = "submitTokenCard"
    submitCheckButton = "submitCheck"
    submitCheckTokenButton = "submitTokenCheck"
    submitSimpleCheckButton = "submitSimpleCheck"
    submitCheckConversionButton = "submitCheckConversion"
    submitDignifiButton = "submitDigniFi"

    noSaveTokenButton = "noSaveToken"
    closeInvoiceButton = "closeInvoice"

    okAlertButton = "okAlert"

    acceptButton = "/html/body/div/div/div/main/div[2]/div/div/div/form/div[2]/button/span[1]"

    # Labels
    titleLabel = "p[type='title']"
    errorLabel = ".error"
    emailErrorLabel = "/html/body/div/div/div/main/div[2]/div/div/div/form/div[1]/div[3]/div/p"
    emailEbppInvoiceLabel = "/html/body/div/div/div/main/div[2]/div/div/div/form/div[1]/div[1]/div/p"

    approvedTitle = ".header > h2"

    transactionTypeLabel = "body > div.card > div.body > span:nth-child(1)"
    amountLabel = "body > div.card > div.body > span:nth-child(3)"
    authCodeLabel = "body > div.card > div.body > span:nth-child(5)"
    transactionIdLabel = "body > div.card > div.body > span:nth-child(7)"
    resultLabel = "body > div.card > div.body > span:nth-child(9)"

    cashDrawerOpenedLabel = "body > div.card > div.body > span"

    cashAmountLabel = "ItemAmountCash"
    cardAmountLabel = "div[data-amount='trx'] > div:nth-child(3) >span"

    userInformationLabel = 'span[data-session="LABEL"]'
    totalLabel = 'div[data-type="LABEL"] > span'

    titleSaveToken = "#createTokenForm > legend"

    # Receipt
    transTitleReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > h2"
    dateReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(2) > span"
    amountReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(3) > span"
    cardNumberReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(4)" \
                             " > span"
    merchantIdReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(5)" \
                             " > span"
    authCodeReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(7) > span"
    processedAsReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(8) > " \
                              "span"
    referenceNumberReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > " \
                                  "div:nth-child(9) > span"
    referenceNumberSaleReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > " \
                                      "div:nth-child(10) > span"
    invoiceReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(11) > span"
    responseMsgReceiptLabel = " div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(12) " \
                              "> span"
    entryMethodReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(13)" \
                              " > span"
    entryMethodSaleReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > " \
                                  "div:nth-child(14) > span"
    clientIdReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(18) > span"
    tokenIdReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(19) > span"
    userIdReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyRight > div > div:nth-child(20) > span"
    avsReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyLeft > div > div:nth-child(1) > span"
    zipCodeReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyLeft > div > div:nth-child(2) > span"
    nameOnCardReceiptLabel = "div.layaoutInvoiceBigBody > div.layaoutInvoiceBigBodyLeft > h2:nth-child(3)"

    # Check receipt
    referenceNumberCheckReceiptLabel = "referneceNumberCheckInvoice"
    authNumberCheckReceiptLabel = "authNumberCheckInvoice"
    messageCheckReceiptLabel = "messageCheckInvoice"
    messageGuarantee1CheckLabel = "messageGuaranteeCheckInvoice1"
    messageGuarantee2CheckLabel = "messageGuaranteeCheckInvoice2"

    # Simple check receipt
    referenceNumberSimpleCheckReceiptLabel = "referneceNumberSimpleCheckInvoice"
    authCodeSimpleCheckReceiptLabel = "authNumberSimpleCheckInvoice"
    messageSimpleCheckReceiptLabel = "messageSimpleCheckInvoice"

    # Dignifi check receipt
    referenceNumberDignifiReceiptLabel = "referneceNumberDignifiInvoice"
    authCodeDignifiReceiptLabel = "authNumberDignifiInvoice"
    messageDignifiReceiptLabel = "messageDignifiInvoice"

    # Modals
    infoModal = "div[role='dialog']"
    cashOpsModal = "/html/body/div[6]/div[2]"

    # Menu items
    reportMenuItem = "#root > div > div > div.MuiDrawer-root.MuiDrawer-docked > div > ul > div:nth-child(4)"

    # Links
    menu = "#app>div>nav>div.v-navigation-drawer__content>div>div:nth-child(MENU)"
    subMenu =  "#app>div>nav>div.v-navigation-drawer__content>div>div:nth-child(MENU)>div>div.v-list-group__items>a:nth-child(SUBMENU)"
    subMenuLinks = "a[href='#/TRANS']"

    # Frame
    cashOpsFrame = "CenposIFrame"

    # Table
    tokenItemTable = "td[title='TOKEN']"
