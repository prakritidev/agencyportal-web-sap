def login(driver, company_id, agency_id, email, password):
    driver.get("https://agencysvc10.successfactors.com/home")
    # Wating page to load after get request
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__xmlview0--companyId-inner"]'))
        )
    except Exception as e:
        print("Internet Too Slow...not able to check credentials")
        driver.close()
        pass

    #  CompanyID
    driver.find_element_by_xpath(
        '//*[@id="__xmlview0--companyId-inner"]').send_keys(company_id)

    # Agency ID
    driver.find_element_by_xpath(
        '//*[@id="__xmlview0--agencyId-inner"]').send_keys(agency_id)

    # Email
    driver.find_element_by_xpath(
        '//*[@id="__xmlview0--userEmail-inner"]').send_keys(email)

    # Password
    driver.find_element_by_xpath(
        '//*[@id="__xmlview0--password-inner"]').send_keys(password)

    # Password
    driver.find_element_by_xpath(
        '//*[@id="__xmlview0--loginButton"]').click()

    # Waiting page to load after login
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__xmlview1--jobReqListSearchBar-I"]'))
        )
    finally:
        print("Internet Too Slow...This will take some time to finish")
        pass
    return driver
