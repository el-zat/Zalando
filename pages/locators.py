from selenium.webdriver.common.by import By


class BasePageLocators:
    CAT_WOMEN = (By.CSS_SELECTOR, ".z-navicat-header_genderItem:nth-child(1) .z-navicat-header_gender")
    CAT_MEN = (By.CSS_SELECTOR, ".z-navicat-header_genderItem:nth-child(2) .z-navicat-header_gender")
    CAT_KIDS = (By.CSS_SELECTOR, ".z-navicat-header_genderItem:nth-child(3) .z-navicat-header_gender")
    PROD_TYPE_CLOTHES = (By.CSS_SELECTOR, ".z-navicat-header_categoryListElement:nth-child(3)")
    PROD_TYPE_SHOES = (By.CSS_SELECTOR, ".z-navicat-header_categoryListElement:nth-child(4)")
    PROD_TYPE_SPORT = (By.CSS_SELECTOR, ".z-navicat-header_categoryListElement:nth-child(5)")
    PROD_TYPE_ACCESSOIRES = (By.CSS_SELECTOR, ".z-navicat-header_categoryListElement:nth-child(6)")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".z-navicat-header_navToolItem-bag")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".z-navicat-header_navToolItem-wishlist")
    HOME_BUTTON = (By.CSS_SELECTOR, ".z-navicat-header_svgLogo")
    NUMBER_ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".z-navicat-header_navToolItem-bag .jGBT93")
    NUMBER_ITEMS_IN_WISHLIST = (By.CSS_SELECTOR, ".z-navicat-header_navToolItem-wishlist .jGBT93")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".z-navicat-header_navToolItem-profile")
    ACCEPT_BANNER = (By.CSS_SELECTOR, "[id='uc-btn-accept-banner']")

class MainPageLocators:
    FLOAT_WINDOW = (By.CSS_SELECTOR, "[style='overflow-x:hidden']")
    PRODUCT_TSHIRT = (By.CSS_SELECTOR, "[data-trckng-component='_zt7w79yX845c0fNK~w5F']")
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, "[data-trckng-component='_zt7w79yX845c0fNK~w5F'] svg]")


class ProductPageLocators:
    RESPONSES = (By.CSS_SELECTOR, "[data-testid='pdp-rating']")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".z-pdp__dx_cta_container")
    ALL_PICTURES_OF_PRODUCT_TSHIRT = (By.CSS_SELECTOR, ".tFeaYX .LNpJnX:nth-child(1) .WdG8Bv")
    PRICE_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".tFeaYX .vSgP6A .pVrzNP")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".z-coast-base__article-price__wrapper .z-2-text-black")

    CHOOSE_SIZE_BUTTON = (By.CSS_SELECTOR, "#picker-trigger")
    SIZE_XS = (By.CSS_SELECTOR, "[name='size-picker-form'] .EJ4MLB:nth-child(1)")
    NUMBER_OF_ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".z-coast-cart__cart--first-article-group .z-2-dropdown--mode-native")
    CHOOSE_2_ITEM = (By.CSS_SELECTOR, ".z-2-dropdown__control [value='2']")


class BasketPageLocators:
    DELETE_ITEM_IN_BASKET = (By.CSS_SELECTOR, ".z-coast-cart__cart--first-article-group [data-id='article-remove']")
    REMOVE_ITEM_TO_WISHLIST = (By.CSS_SELECTOR, ".z-coast-cart__cart--first-article-group [data-id='article-move-to-wishlist']")
    GO_TO_PAYMENT = (By.CSS_SELECTOR, ".z-coast-cart__cart__sticky .z-1-button--button")
    PAYMEMT_METHODS = (By.CSS_SELECTOR, ".z-coast-cart__cart__cart-tiles .z-coast-base__tile--white:nth-child(3)")


class LoginPageLocators:
    EMAIL_FORM = (By.CSS_SELECTOR, ".lny_2XQjh:nth-child(1) .xRIrkR .Vn-7c-")
    PASSWORD_FORM = (By.CSS_SELECTOR, ".lny_2XQjh:nth-child(2) .Vn-7c-")
    LOGIN = (By.CSS_SELECTOR, ".lny_2XQjh:nth-child(3) .mo6ZnF")
