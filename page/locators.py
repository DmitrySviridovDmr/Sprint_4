from selenium.webdriver.common.by import By


class MainPageLocators:
    yandex_url = "https://yandex.ru/"
    main_url = "https://qa-scooter.praktikum-services.ru/"
    confirm_cookies = (By.ID, "rcc-confirm-button")
    yandex_button = (By.CSS_SELECTOR,
                     "#root > div > div > div.Header_Header__214zg > div.Header_Logo__23yGT > a.Header_LogoYandex__3TSOI")
    order_button_header = (By.CSS_SELECTOR,
                           "#root > div > div > div.Header_Header__214zg > div.Header_Nav__AGCXC > button.Button_Button__ra12g")
    order_button_middle = (By.CSS_SELECTOR,
                           "#root > div > div > div.Home_ThirdPart__LSTEE > div.Home_RoadMap__2tal_ > div.Home_FinishButton__1_cWm > button")
    # questions block
    how_much_cost = (By.CSS_SELECTOR, "#accordion__heading-0")
    answer_how_much_cost = (By.CSS_SELECTOR, "#accordion__panel-0")
    couple_scooters = (By.CSS_SELECTOR, "#accordion__heading-1")
    answer_couple_scooters = (By.CSS_SELECTOR, "#accordion__panel-1")
    rent_time = (By.CSS_SELECTOR, "#accordion__heading-2")
    answer_rent_time = (By.CSS_SELECTOR, "#accordion__panel-2")
    rent_today = (By.CSS_SELECTOR, "#accordion__heading-3")
    answer_rent_today = (By.CSS_SELECTOR, "#accordion__panel-3")
    prolongation_rent = (By.CSS_SELECTOR, "#accordion__heading-4")
    answer_prolongation_rent = (By.CSS_SELECTOR, "#accordion__panel-4")
    charger_with_scooter = (By.CSS_SELECTOR, "#accordion__heading-5")
    answer_charger_with_scooter = (By.CSS_SELECTOR, "#accordion__panel-5")
    cancel_order = (By.CSS_SELECTOR, "#accordion__heading-6")
    answer_cancel_order = (By.CSS_SELECTOR, "#accordion__panel-6")
    behind_MKAD = (By.CSS_SELECTOR, "#accordion__heading-7")
    answer_behind_MKAD = (By.CSS_SELECTOR, "#accordion__panel-7")


class OrderPageLocators:
    order_url = f"{MainPageLocators.main_url}order"
    scooter_button = (By.CSS_SELECTOR, "#root > div > div.Header_Header__214zg > div.Header_Logo__23yGT > a.Header_LogoScooter__3lsAR")
    first_name = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div:nth-child(1) > input")
    last_name = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div:nth-child(2) > input")
    address = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div:nth-child(3) > input")
    station = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div:nth-child(4) > div > div > input")
    phone = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div:nth-child(5) > input")
    next_button = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_NextButton__1_rCA > button")
    date_field = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div.Order_MixedDatePicker__3qiay > div.react-datepicker-wrapper > div > input")
    rent_period = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div.Dropdown-root > div > div.Dropdown-placeholder")
    one_day = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div.Dropdown-root.is-open > div.Dropdown-menu > div:nth-child(1)")
    three_days = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div.Dropdown-root.is-open > div.Dropdown-menu > div:nth-child(3)")
    black_color_scooter = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div.Order_Checkboxes__3lWSI > label:nth-child(2)")
    grey_color_scooter = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div.Order_Checkboxes__3lWSI > label:nth-child(4)")
    comment_for_courier = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Form__17u6u > div.Input_InputContainer__3NykH > input")
    order_button = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Buttons__1xGrp > button:nth-child(2)")
    yes_button = (By.CSS_SELECTOR, "#root > div > div.Order_Content__bmtHS > div.Order_Modal__YZ-d3 > div.Order_Buttons__1xGrp > button:nth-child(2)")
    success_order = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")
    watch_status = (By.CSS_SELECTOR, ".Order_NextButton__1_rCA > button:nth-child(1)")
