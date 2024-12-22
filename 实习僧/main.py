from playwright.sync_api import sync_playwright
from mysql import MySqlCommand

mysqlCommand = MySqlCommand()
mysqlCommand.connectionMysql()
with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    )
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.shixiseng.com/")
    page.locator('img.closeOpen').click()
    page.locator('input.nonal').fill('web前端')
    with context.expect_page() as new_page_info:
        page.locator('input.form--button').click()

    newPage = new_page_info.value

    # 等待目标元素加载完成
    newPage.wait_for_selector('a.title.ellipsis.font', timeout=5000)  # 最长等待5秒
    page_btn = newPage.locator('li.number')
    times = int(page_btn.nth(page_btn.count() - 1).text_content()) - 1
    switchBtn = newPage.locator('button.btn-next')
    print(times)
    for cs in range(times):
        elements_count = newPage.locator('a.title.ellipsis.font').count()
        listData = newPage.locator('a.title.ellipsis.font')
        print(f"第{cs+1}页")
        for i in range(elements_count):
            url = listData.nth(i).get_attribute('href')
            page3 = context.new_page()
            page3.goto(url)
            page3.wait_for_selector('.new_job_name span', timeout=3000)
            # 使用 try-except 获取元素内容，如果获取失败则设置默认值
            #1岗位名称

            try:
                title = page3.locator(
                    '.new_job_name span').text_content() or "N/A"
            except Exception:
                title = "N/A"

            #2最近更新时间
            try:
                update_time = page3.locator(
                    '.job_date span.cutom_font').text_content() or "N/A"
            except Exception:
                update_time = "N/A"

            #3日薪
            try:
                day_salary = page3.locator(
                    '.job_money.cutom_font').text_content() or "N/A"
            except Exception:
                day_salary = "N/A"

            #4工作地点
            try:
                work_position = page3.locator(
                    '.job_position').text_content() or "N/A"
            except Exception:
                work_position = "N/A"

            #5学历要求
            try:
                academic = page3.locator(
                    '.job_academic').text_content() or "N/A"
            except Exception:
                academic = "N/A"

            #6每周工作时间
            try:
                work_week = page3.locator('.job_week').text_content() or "N/A"
            except Exception:
                work_week = "N/A"

            #7实习要求时间
            try:
                practice_time = page3.locator(
                    '.job_time').text_content() or "N/A"
            except Exception:
                practice_time = "N/A"

            #8职位描述
            try:
                job_detail = page3.locator(
                    '.job_part .job_detail').text_content() or "N/A"
            except Exception:
                job_detail = "N/A"

            #9具体工作地点
            try:
                location_detail = page3.locator(
                    'span.com_position').text_content() or "N/A"
            except Exception:
                location_detail = "N/A"

            #10投递要求
            try:
                require = page3.locator('.con-job') or "N/A"
                requirement = require.nth(1).text_content()
            except Exception:
                requirement = "N/A"

            # 打印爬取到的内容
            data = {
                "page_url": url,
                "title": title,
                "update_time": update_time,
                "day_salary": day_salary,
                "work_position": work_position,
                "academic": academic,
                "work_week": work_week,
                "practice_time": practice_time,
                "job_detail": job_detail,
                "location_detail": location_detail,
                "requirement": requirement,
            }

            mysqlCommand.insertData(page_url=url, data=data)
            page3.close()
            print("插入成功~")
        switchBtn.click()
        newPage.wait_for_timeout(1000)
    browser.close()
