pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [r"(.*)mua bảo hiểm", ["Dạ hiện tại e đang bán tất cả các mặt hàng bhnt..."]],
    [r"tôi tên là (.*)", ["Xin chào %1. Em có thể giúp gì được anh chị ạ?"]],
    [r"Hi|xin chào|ê", ["Xin chào"]],
    [r"(bạn|em) tên gì?", ["Em là Chat bot đáng yêu!!!"]],
    [r"em mấy tuổi rồi?", ["Hmmmm! E chỉ là bot thôi ạ!"]],
    [r"(.*) sản phẩm gì?", ["Gì em cũng bán ạ!!!"]],
    [r"(.*)thời gian cân nhắc", [
        "Thời gian cân nhắc là khoảng thời gian 21 ngày kể từ ngày Khách hàng ký nhận bộ hợp đồng, Khách hàng có thể xem xét lại một cách cẩn thận về các Quy tắc và Điều khoản của sản phẩm đã tham gia. Khách hàng có quyền từ chối tham gia bảo hiểm hoặc thay đổi/ điều chỉnh hợp đồng cho phù hợp với nhu cầu của mình."]],
    [r"(.*)bảo hiểm tạm thời", [
        "Bảo hiểm tạm thời là quyền lợi bảo hiểm cung cấp trong trường hợp Khách hàng bị tử vong do tai nạn trong thời gian Sun Life Việt Nam đang xem xét chấp thuận bảo hiểm cho Khách hàng."]],
    [r"(.*)bảo hiểm nhân thọ là gì", [
        "Bảo hiểm nhân thọ là: \nLoại hình bảo hiểm mà đối tượng được bảo hiểm là con người,\nKế hoạch hữu hiệu để bảo vệ an toàn tài chính cho khách hàng tham gia bảo hiểm và gia đình họ khi không may gặp phải rủi ro (như tử vong, tai nạn, bệnh hiểm nghèo…). \nBên cạnh đó, bảo hiểm nhân thọ còn giúp khách hàng tiết kiệm và đầu tư một cách kỷ luật để thực hiện những kế hoạch trong tương lai (như đảm bảo tương lai học vấn cho con, tích lũy để mua nhà, mua xe… hoặc có tiền để nghỉ hưu an nhàn)."]],
    [r"(.*)người thụ hưởng là gì", ["Em chưa học khái niệm này ạ"]],
    [r"(.*)hủy ngang là gì?",
     ["Bên mua bảo hiểm có thể yêu cầu Sun Life Việt Nam hủy bỏ hoặc thay đổi Người thụ hưởng bất cứ lúc nào"]],
    [r"(.*)giá trị hoàn lại là gì?", [
        "Giá trị hoàn lại là số tiền mà Bên mua bảo hiểm sẽ nhận được nếu hủy bỏ hợp đồng trong thời gian hợp đồng có hiệu lực, sau khi trừ đi các khoản nợ."]],
    [r"(bảo hiểm nhân thọ|bhnt) có lợi ích gì|lợi ích gì khi tham gia (bảo hiểm nhân thọ|bhnt)",
     ["Những rủi ro bất trắc trong cuộc sống là điều không ai mong muốn nhưng cũng không thể tránh khỏi."]],
    [r"công ty phá sản thì sao|tôi có mất tiền không", [
        "Theo quy định của Luật kinh doanh bảo hiểm, công ty bảo hiểm phải trích lập dự phòng, báo cáo dự phòng và tình hình tài chính của công ty cho Bộ Tài chính theo định kỳ."]],

    [r"quit", ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]],

    [r"(.*)gửi tiết kiệm ở ngân hàng(.*)", ["Nói chung, BHNT vừa có tính bảo vệ, vừa có tính tiết kiệm. Nếu có rủi ro xảy ra, thì quyền lợi được chi trả sẽ là phao an toàn tài chính cho gia đình. Nếu may mắn không có rủi ro xảy ra thì giá trị hợp đồng bảo hiểm chính là khoản tiết kiệm của khách hàng.  \nYếu tố bảo vệ khi chẳng may có rủi ro xảy ra chính là điểm khác biệt cơ bản giữa tham gia BHNT và gửi tiết kiệm tại ngân hàng. Khi hợp đồng BHNT được công ty bảo hiểm chấp thuận, người tham gia bảo hiểm đã ngay lập tức được bảo vệ an toàn tài chính với số tiền bảo hiểm ghi trên hợp đồng. Khi có sự kiện bảo hiểm xảy ra, công ty bảo hiểm sẽ chi trả đầy đủ quyền lợi bảo hiểm theo quy định của hợp đồng, bất kể là khách hàng đã tham gia bao lâu, đã nộp bao nhiêu phí bảo hiểm. Trong khi đó, ngân hàng chỉ có trách nhiệm với số tiền mà khách hàng đã gửi vào, cho dù có hay không có rủi ro xảy ra với khách hàng.  \nMột điểm khác biệt nữa cũng cần nhắc tới là BHNT giúp khách hàng tiết kiệm một cách kỷ luật hơn (qua việc đóng phí bảo hiểm định kỳ), và vì thế, ít bị cám dỗ bởi các chi tiêu tùy hứng."]],
    [r"(.*)trong gia đình(.*)mua bảo hiểm cho ai",
        ["Lý tưởng thì trong một gia đình thành viên nào cũng nên có bảo hiểm nhân thọ (BHNT) với sản phẩm và số tiền bảo hiểm phù hợp.  \nTuy nhiên, xuất phát từ ý nghĩa cơ bản của BHNT là đảm bảo an toàn tài chính, nên trong một gia đình người đầu tiên nên tham gia bảo hiểm nhân thọ là người trụ cột (tức là người mang lại nguồn thu nhập chính cho gia đình). Bằng cách đó, nếu không may có rủi ro xảy ra với người trụ cột, cả gia đình sẽ không lâm vào hoàn cảnh khó khăn. \nVới mong muốn mang lại sự bảo vệ tốt nhất cho người dân Việt Nam, khi khách hàng có hợp đồng bảo hiểm nhân thọ với AIA , tất cả các thành viên gia đình của khách hàng (cha mẹ, vợ/chồng, con, …) có thể tham gia sản phẩm bổ sung trong cùng hợp đồng này. "]],
    [r"tham gia(.*)(mệnh giá|giá)(.*)bao nhiêu",["Thông thường, sản phẩm bảo hiểm và số tiền bảo hiểm phù hợp được xác định dựa trên các yếu tố quyết định sau: \nMục tiêu mà khách hàng dự tính thực hiện sau một khoảng thời gian xác định, \nSố tiền tối thiểu mà khách hàng cần để thực hiện mục tiêu đó, \nKhách hàng cần được bảo vệ trước những rủi ro nào, và \nKhả năng đóng phí bảo hiểm (tiết kiệm) của khách hàng…  \nTại AIA Việt Nam, các đại lý bảo hiểm/chuyên viên hoạch định tài chính của chúng tôi được trang bị công cụ “Kiểm tra sức khỏe tài chính” để giúp khách hàng xác định sản phẩm bảo hiểm cũng như số tiền bảo hiểm phù hợp với nhu cầu và tình hình tài chính của bản thân và gia đình họ.  \nNếu nói về con số phỏng chừng, các chuyên gia tài chính cho rằng, để đảm bảo an toàn tài chính cho gia đình, một người trụ cột nên được bảo hiểm với số tiền khoảng 10 lần thu nhập hàng năm của mình."]],


]