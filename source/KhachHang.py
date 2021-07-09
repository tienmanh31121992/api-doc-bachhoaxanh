"""
@api {post} /customers/actions/register Đăng ký
@apiName Đăng_ký
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng đăng ký tài khoản


@apiHeader {String} Content-Type <mark>application/json</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json"
}


@apiParam (Body) {String} customer_name Tên khách hàng
@apiParam (Body) {Number=0,1} gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiParam (Body) {String} customer_phone Số điện thoại
@apiParam (Body) {String} password Mật khẩu
@apiParam (Body) {String} address Địa chỉ khách hàng
@apiParam (Body) {Date}   [date_of_birth] Ngày sinh
@apiParam (Body) {String} [email] Địa chỉ thư điện tử
@apiParam (Body) {String} [avatar_link] Đường dẫn lưu ảnh đại diện
@apiParam (Body) {String} [guardian_name] Tên người giám hộ
@apiParam (Body) {String} [indentity_id] Số chứng minh thư, căn cước, hộ chiếu
@apiParam (Body) {Date}   [certify_date] Ngày cấp CMT, CCCD, HC
@apiParam (Body) {String} [certify_place] Nơi cấp CMT, CCCD, HC
@apiParam (Body) {Number} province_id ID tỉnh/thành phố
@apiParam (Body) {Number} district_id ID quận/huyện
@apiParam (Body) {Number} block_id ID xã/phường

@apiParamExample {JSON} Body request:
{
    "customer_name": "Tiến Mạnh",
    "gender": 1,
    "customer_phone": "0123456789",
    "password": "a1b2c3A@",
    "address": "Số 9, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
    "date_of_birth": "31/12/1992",
    "email": "asdasdasf@gmail.com",
    "avatar_link": "avatar1.jpg",
    "guardian_name": null,
    "indentity_id": "HC000001VN",
    "certify_date": "12/12/2009",
    "certify_place": "Hải Dương",
    "province_id": 1,
    "district_id": 2,
    "block_id": 3
}


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Đăng ký tài khoản thành công!"
}


@apiError 412-PreconditionFailed Lỗi kiểm tra điều kiện
<ul>
    <li><code>code:</code> 412</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 412:
{
    "code": 412,
    "message": "Tài khoản đã tồn tại!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi đăng ký: Mô tả lỗi."
}
"""

"""
@api {post} /customers/actions/login Đăng nhập
@apiName Đăng_nhập
@apiGroup Khách_hàng
@apiVersion  1.0.0
@apiDescription Khách hàng đăng nhập vào hệ thống


@apiHeader {String} Content-Type <mark>application/json</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json"
}


@apiParam (Body) {String} customer_phone Số điện thoại khách hàng
@apiParam (Body) {String} password Mật khẩu đăng nhập

@apiParamExample {JSON} Body request:
{
    "customer_phone": "0123456789",
    "password": "a1b2c3A@"
}


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.mesage Thông báo kết quả
@apiSuccess {String} O.token Chuỗi Token
@apiSuccess {Object} O.data Thông tin của khách hàng
@apiSuccess {Number} O.data.customer_id ID khách hàng
@apiSuccess {String} O.data.customer_code Mã khách hàng
@apiSuccess {String} O.data.customer_name Tên khách hàng
@apiSuccess {Number} O.data.gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiSuccess {String} O.data.customer_phone Số điện thoại
@apiSuccess {String} O.data.customer_address Địa chỉ khách hàng
@apiSuccess {Date}   O.data.date_of_birth Ngày sinh
@apiSuccess {String} O.data.avatar_link Đường dẫn lưu ảnh đại diện
@apiSuccess {String} O.data.email Địa chỉ thư điện tử
@apiSuccess {String} O.data.guardian_name Tên người giám hộ
@apiSuccess {String} O.data.indentity_id Số chứng minh thư, căn cước, hộ chiếu
@apiSuccess {Date}   O.data.certify_date Ngày cấp CMT, CCCD, HC
@apiSuccess {String} O.data.certify_place Nơi cấp CMT, CCCD, HC
@apiSuccess {Number} O.data.province_id ID tỉnh/thành phố
@apiSuccess {Number} O.data.district_id ID quận/huyện
@apiSuccess {Number} O.data.block_id ID xã/phường


@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Đăng nhập thành công!",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
    "data": {
        "customer_id": 10,
        "customer_code": "A0000001",
        "customer_name": "Tiến Mạnh",
        "gender": 1,
        "customer_phone": "0123456789",
        "customer_address": "Số 9, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
        "date_of_birth": "31/12/1992",
        "email": "asdasdasf@gmail.com",
        "avatar_link": "avatar1.jpg",
        "guardian_name": null,
        "indentity_id": "HC000001VN",
        "certify_date": "12/12/2009",
        "certify_place": "Hải Dương",
        "province_id": 1,
        "district_id": 2,
        "block_id": 3
    }
}


@apiError 403-Forbidden Truy cập dữ liệu bị từ chối
<ul>
    <li><code>code:</code> 403</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Lỗi truy cập dữ liệu không tồn tại
<ul>
    <li><code>code:</code> 404</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 412-PreconditionFailed Lỗi khi kiểm tra dữ liệu
<ul>
    <li><code>code:</code> 412</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 403:
{
    "code": 403,
    "message": "Tài khoản đang bị khóa!"
}
@apiErrorExample {JSON} Error 404:
{
    "code": 404,
    "message": "Tài khoản không tồn tại!"
}
@apiErrorExample {JSON} Error 412:
{
    "code": 412,
    "message": "Mật khẩu không đúng!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi đăng nhập: Mô tả lỗi."
}
"""

"""
@api {patch} /customers Cập nhật thông tin
@apiName Cập_nhật_thông_tin
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng cập nhật thông tin tài khoản


@apiHeader {String} Content-Type <mark>application/json</mark>
@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
}


@apiParam (Body) {Number} customer_id ID khách hàng
@apiParam (Body) {String} customer_code Mã khách hàng
@apiParam (Body) {String} customer_name Tên khách hàng
@apiParam (Body) {String} customer_phone Số điện thoại
@apiParam (Body) {String} customer_address Địa chỉ khách hàng
@apiParam (Body) {Date}   [date_of_birth] Ngày sinh
@apiParam (Body) {String} [avatar_link] Đường dẫn lưu ảnh đại diện
@apiParam (Body) {String} [email] Địa chỉ thư điện tử
@apiParam (Body) {Number=0,1} gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiParam (Body) {String} [guardian_name] Tên người giám hộ
@apiParam (Body) {String} [indentity_id] Số chứng minh thư, căn cước, hộ chiếu
@apiParam (Body) {Date}   [certify_date] Ngày cấp CMT, CCCD, HC
@apiParam (Body) {String} [certify_place] Nơi cấp CMT, CCCD, HC
@apiParam (Body) {Number} province_id ID tỉnh/thành phố
@apiParam (Body) {Number} district_id ID quận/huyện
@apiParam (Body) {Number} block_id ID xã/phường

@apiParamExample {JSON} Body request:
{
    "customer_id": 10,
    "customer_code": "A0000001",
    "customer_name": "Phạm Tiến Mạnh",
    "customer_phone": "0123456789",
    "customer_address": "Số 11, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
    "date_of_birth": "31/12/1992",
    "avatar_link": "avatar1.jpg",
    "email": "asdasdasf@gmail.com",
    "gender": 1,
    "guardian_name": null,
    "indentity_id": "HC000001VN",
    "certify_date": "10/10/2010",
    "certify_place": "Hải Dương",
    "province_id": 4,
    "district_id": 5,
    "block_id": 6
}


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả
@apiSuccess {Object} O.data Thông tin khách hàng
@apiSuccess {Number} O.data.customer_id ID khách hàng
@apiSuccess {String} O.data.customer_code Mã khách hàng
@apiSuccess {String} O.data.customer_name Tên khách hàng
@apiSuccess {String} O.data.customer_phone Số điện thoại
@apiSuccess {String} O.data.customer_address Địa chỉ khách hàng
@apiSuccess {Date}   O.data.date_of_birth Ngày sinh
@apiSuccess {String} O.data.avatar_link Đường dẫn lưu ảnh đại diện
@apiSuccess {String} O.data.email Địa chỉ thư điện tử
@apiSuccess {Number} O.data.gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiSuccess {String} O.data.guardian_name Tên người giám hộ
@apiSuccess {String} O.data.indentity_id Số chứng minh thư, căn cước, hộ chiếu
@apiSuccess {Date}   O.data.certify_date Ngày cấp CMT, CCCD, HC
@apiSuccess {String} O.data.certify_place Nơi cấp CMT, CCCD, HC
@apiSuccess {Number} O.data.province_id ID tỉnh/thành phố
@apiSuccess {Number} O.data.district_id ID quận/huyện
@apiSuccess {Number} O.data.block_id ID xã/phường

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Cập nhật thông tin thành công!",
    "data": {
        "customer_id": 1,
        "customer_code": "A0000001",
        "customer_name": "Phạm Tiến Mạnh",
        "customer_phone": "0123456789",
        "customer_address": "Số 11, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
        "date_of_birth": "31/12/1992",
        "avatar_link": "avatar2.jpg",
        "email": "asdasdasf@gmail.com",
        "gender": 1,
        "guardian_name": null,
        "indentity_id": "HC000001VN",
        "certify_date": "10/10/2010",
        "certify_place": "Hải Dương",
        "province_id": 4,
        "district_id": 5,
        "block_id": 6
    }
}


@apiError 401-Unauthorized Token hết hạn hoặc không hợp lệ.
<ul>
    <li><code>code:</code> 401</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 401:
{
    "code": 401,
    "message": "Token hết hạn hoặc không hợp lệ. Vui lòng đăng nhập lại!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi cập nhật thông tin: Mô tả lỗi."
}
"""

"""
@api {post} /customers/actions/change-password Đổi mật khẩu
@apiName Đổi_mật_khẩu
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng thay đổi mật khẩu


@apiHeader {String} Content-Type <mark>application/json</mark>
@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
}


@apiParam (Body) {Number} customer_id ID khách hàng
@apiParam (Body) {String} customer_code Mã khách hàng
@apiParam (Body) {String} customer_phone Số điện thoại
@apiParam (Body) {String} password Mật khẩu hiện tại
@apiParam (Body) {String} new_password Mật khẩu mới

@apiParamExample  {JSON} Body request:
{
    "customer_id": 10,
    "customer_code": "A0000001",
    "customer_phone": "0123456789",
    "password": "a1b2c3A@",
    "new_password": "9m8n7b#"
}


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Đổi mật khẩu thành công. Vui lòng đăng nhập lại!"
}

@apiError 401-Unauthorized Token hết hạn hoặc không hợp lệ.
<ul>
    <li><code>code:</code> 401</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 412-PreconditionFailed Lỗi kiểm tra điều kiện
<ul>
    <li><code>code:</code> 412</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 401:
{
    "code": 401,
    "message": "Token hết hạn hoặc không hợp lệ. Vui lòng đăng nhập lại!"
}
@apiErrorExample {JSON} Error 412:
{
    "code": 412,
    "message": "Mật khẩu hiện tại không đúng!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi đổi mật khẩu: Mô tả lỗi."
}
"""


"""
@api {post} /customers/actions/order-giftcards Đặt mua phiếu mua hàng
@apiName Mua_phiếu_mua_hàng
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng đặt mua phiếu mua hàng điện tử


@apiHeader {String} Content-Type <mark>application/json</mark>
@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
}


@apiParam (Body) {Number} customer_id ID khách hàng
@apiParam (Body) {Number} gift_card_id ID phiếu mua hàng
@apiParam (Body) {Number} phone Số điện thoại nhận mã sử dụng phiếu mua hàng
@apiParam (Body) {Number} quantity Số lượng

@apiParamExample Body request:
{
    "customer_id": 10,
    "gift_card_id": 1,
    "customer_phone": "0123456789",
    "quantity": 2
}


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Đặt mua phiếu mua hàng thành công!"
}


@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 401-Unauthorized Token hết hạn hoặc không hợp lệ.
<ul>
    <li><code>code:</code> 401</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 400:
{
    "code": 400,
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 401:
{
    "code": 401,
    "message": "Token hết hạn hoặc không hợp lệ. Vui lòng đăng nhập lại!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi đặt mua phiếu mua hàng: Mô tả lỗi."
}
"""


"""
@api {get} /customers/<customer_id>/giftcards Xem phiếu mua hàng đang sở hữu
@apiName Xem_phiếu_mua_hàng
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Lấy danh sách phiếu mua hàng khách hàng đang sở hữu


@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

@apiHeaderExample {JSON} Header request:
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
}


@apiParam (Path) {Number} customer_id <mark>ID khách hàng</mark>

@apiParam {String=end_time,value} sort=-end_time <mark>Sắp xếp dữ liệu. Ví dụ: <code>sort=+field_1,-field_2,field_3</code></mark>
<ul>
    <li><code>+:</code> Sắp xếp tăng dần</li>
    <li><code>-:</code> Sắp xếp giảm dần</li>
    <li><code>Mặc định:</code> Sắp xếp tăng dần</li>
</ul>

@apiParamExample URL request:
{host}/api/v1.0/customers/10/giftcards?sort=-end_time


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin phiếu mua hàng
@apiSuccess {Number}    O.data.gift_card_id ID phiếu mua hàng khách hàng đang sở hữu
@apiSuccess {String}    O.data.gift_card_code Mã sử dụng của phiếu mua hàng
@apiSuccess {Date}      O.data.end_time Thời hạn phiếu mua hàng của khách hàng
@apiSuccess {Number}    O.data.value Giá trị của phiếu mua hàng

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy thông tin phiếu mua hàng thành công!",
    "data": [
        {
            "gift_card_id": 1,
            "gift_card_code": "PHM1000K-0626565",
            "end_time": "31/12/2021",
            "value": 1000000
        },
        {
            "gift_card_id": 1,
            "gift_card_code": "PHM1000K-56464564",
            "end_time": "31/12/2021",
            "value": 1000000
        },
        {
            "gift_card_id": 2,
            "gift_card_code": "PHM2000K-6546464565",
            "end_time": "31/12/2022"
            "value": 2000000
        }
    ]
}

@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Không tìm thấy dữ liệu.
<ul>
    <li><code>code:</code> 404</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 400:
{
    "code": 400,
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 404:
{
    "code": 404,
    "message": "Không tìm thấy dữ liệu!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi lấy lịch sử tìm kiếm: Mô tả lỗi."
}
"""


"""
@api {get} /customers/<customer_id>/history-searchs Lịch sử tìm kiếm sản phẩm
@apiName Lịch_sử_tìm_kiếm
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Lấy danh sách từ khóa khách hàng đã tìm kiếm


@apiParam (Path) {Number} customer_id <mark>ID khách hàng</mark>

@apiParam {String=search_string,search_number,searched_at} sort=-searched_at <mark>Sắp xếp dữ liệu. Ví dụ: <code>sort=+field_1,-field_2,field_3</code></mark>
<ul>
    <li><code>+:</code> Sắp xếp tăng dần</li>
    <li><code>-:</code> Sắp xếp giảm dần</li>
    <li><code>Mặc định:</code> Sắp xếp tăng dần</li>
</ul>
@apiParam {Number=≥1} top <mark>Giới hạn số lượng bản ghi

@apiParamExample URL request:
{host}/api/v1.0/customer/10/history-searchs?sort=-searched_at&top=4


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin chuỗi tìm kiếm
@apiSuccess {String}    O.data.search_string Chuỗi tìm kiếm
@apiSuccess {String}    O.data.search_number Số lần tìm kiếm
@apiSuccess {Date}      O.data.searched_at Thời điểm tìm kiếm gần nhất

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy thông tin lịch sử tìm kiếm sản phẩm thành công!",
    "data": [
        {
            "search_string": "thit ga",
            "search_number": 10,
            "searched_at": "01/06/2021"
        },
        {
            "search_string": "trung",
            "search_number": 30,
            "searched_at": "01/06/2021"
        },
        {
            "search_string": "pepsi",
            "search_number": 15,
            "searched_at": "01/06/2021"
        },
        {
            "search_string": "banh keo",
            "search_number": 10,
            "searched_at": "01/06/2021"
        }
    ]
}

@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Không tìm thấy dữ liệu.
<ul>
    <li><code>code:</code> 404</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 400:
{
    "code": 400,
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 404:
{
    "code": 404,
    "message": "Không tìm thấy dữ liệu!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi lấy lịch sử tìm kiếm: Mô tả lỗi."
}
"""

"""
@api {get} /customers/<customer_id>/history-views Lấy danh sách sản phẩm khách hàng đã xem
@apiName Sản_phẩm_đã_xem
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Lấy danh sách sản phẩm khách hàng đã xem


@apiParam (Path) {Number} customer_id <mark>ID khách hàng</mark>

@apiParam {String=view_number,view_at} sort=-view_at <mark>Sắp xếp dữ liệu. Ví dụ: <code>sort=+field_1,-field_2,field_3</code></mark>
<ul>
    <li><code>+:</code> Sắp xếp tăng dần</li>
    <li><code>-:</code> Sắp xếp giảm dần</li>
    <li><code>Mặc định:</code> Sắp xếp tăng dần</li>
</ul>
@apiParam {Number=≥1} top <mark>Giới hạn số lượng bản ghi


@apiParamExample URL request:
{host}/api/v1.0/customers/10/history-views?sort=-view_at&top=4


@apiSuccess {String}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin sản phẩm
@apiSuccess {Number}    O.data.product_id ID sản phẩm
@apiSuccess {String}    O.data.product_code Mã sản phẩm
@apiSuccess {String}    O.data.product_name Tên sản phẩm
@apiSuccess {String}    O.data.thumbnail_link Ảnh đại diện sản phẩm
@apiSuccess {Number}    O.data.price Giá gốc của sản phẩm
@apiSuccess {String}    O.data.unit Đơn vị của sản phẩm
@apiSuccess {String}    O.data.unit_child Đơn vị con của sản phẩm
@apiSuccess {Number}    O.data.quantity Số lượng của sản phẩm
@apiSuccess {Number}    O.data.quantity_child Số lượng con của sản phẩm
@apiSuccess {Date}      O.data.expired_at Ngày hết hạn
@apiSuccess {Number}    O.data.guarantee Bảo hành
@apiSuccess {Number}    O.data.quantity_sold Số lượng đã bán
@apiSuccess {Number}    O.data.views Số lượt xem
@apiSuccess {Number}    O.data.max_buy_number Số lượng mua tối đa
@apiSuccess {Number}    O.data.sale_price Giá bán khuyễn mãi
@apiSuccess {Number}    O.data.sale_percent Phần trăm khuyến mãi
@apiSuccess {Number}    O.data.hot Sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.new Sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.special Sản phẩm đặc biệt
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Object}    O.data.promotion Thông tin khuyến mãi của sản phẩm
@apiSuccess {Number}    O.data.promotion.promotion_id ID khuyến mãi
@apiSuccess {String}    O.data.promotion.promotion_code Mã khuyến mãi
@apiSuccess {String}    O.data.promotion.promotion_name Tên khuyến mãi
@apiSuccess {String}    O.data.promotion.content Nội dung khuyến mãi
@apiSuccess {String}    O.data.promotion.image_link Ảnh khuyến mãi

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách sản phẩm khách hàng đã xem thành công!",
    "data": [
        {
            "product_id": 1,
            "product_code": "SP0001"
            "product_name": "Sản phẩm 1"
            "thumbnail_link": "thumbnail.png"
            "price": 30000,
            "unit": "Thùng",
            "unit_child": "Chai",
            "quantity": 9999,
            "quantity_child": 24,
            "expired_at": "01/01/2023",
            "guarantee": 6,
            "quantity_sold": 9999,
            "views": 10000,
            "max_buy_number": 50,
            "sale_price": 15000,
            "sale_percent": 50,
            "hot": 0,
            "new": 0,
            "promotion": {
                "promotion_id": 1,
                "promotion_code": "KM00050",
                "promotion_name": "Khuyến mãi",
                "content": "Khuyến mãi tất cả sản phẩm ngày hôm nay",
                "image_link": "image.jpg"
            }
        },
        {
            "product_id": 2,
            "product_code": "SP0002"
            "product_name": "Sản phẩm 2"
            "thumbnail_link": "thumbnail.png"
            "price": 30000,
            "unit": "Thùng",
            "unit_child": "Gói",
            "quantity": 9999,
            "quantity_child": 30,
            "expired_at": "01/01/2023",
            "guarantee": 3,
            "quantity_sold": 8798,
            "views": 454,
            "max_buy_number": 50,
            "sale_price": 0,
            "sale_percent": 0,
            "hot": 0,
            "new": 0,
            "promotion": null
        },
        {
            "product_id": 3,
            "product_code": "SP0003"
            "product_name": "Sản phẩm 3"
            "thumbnail_link": "thumbnail.png"
            "price": 30000,
            "unit": "Thùng",
            "unit_child": "Hộp",
            "quantity": 9999,
            "quantity_child": 10,
            "expired_at": "01/01/2023",
            "guarantee": 8,
            "quantity_sold": 564,
            "views": 5456,
            "max_buy_number": 50,
            "sale_price": 15000,
            "sale_percent": 50,
            "hot": 0,
            "new": 0,
            "promotion": {
                "promotion_id": 1,
                "promotion_code": "KM00010",
                "promotion_name": "Khuyến mãi 10",
                "content": "Khuyến mãi tất cả sản phẩm sữa",
                "image_link": "image.jpg"
            }
        },
        {
            "product_id": 4,
            "product_code": "SP0004"
            "product_name": "Sản phẩm 4"
            "thumbnail_link": "thumbnail.png"
            "price": 30000,
            "unit": "Lốc",
            "unit_child": "Chai",
            "quantity": 9999,
            "quantity_child": 6,
            "expired_at": "01/01/2023",
            "guarantee": 12,
            "quantity_sold": 67,
            "views": 6767,
            "max_buy_number": 50,
            "sale_price": 0,
            "sale_percent": 0,
            "hot": 0,
            "new": 0
            "promotion": null
        }
    ]
}

@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Không tìm thấy dữ liệu.
<ul>
    <li><code>code:</code> 404</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 400:
{
    "code": 400,
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 404:
{
    "code": 404,
    "message": "Không tìm thấy dữ liệu!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi lấy lịch sử tìm kiếm: Mô tả lỗi."
}
"""

"""
@api {get} /customers/<customer_id>/history-buys Lấy danh sách sản phẩm khách hàng đã mua
@apiName Sản_phẩm_đã_mua
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Lấy danh sách sản phẩm khách hàng đã mua


@apiParam (Path) {Number} customer_id <mark>ID khách hàng</mark>

@apiParam {String=buy_number,buy_at} sort=-buy_at <mark>Sắp xếp dữ liệu. Ví dụ: <code>sort=+field_1,-field_2,field_3</code></mark>
<ul>
    <li><code>+:</code> Sắp xếp tăng dần</li>
    <li><code>-:</code> Sắp xếp giảm dần</li>
    <li><code>Mặc định:</code> Sắp xếp tăng dần</li>
</ul>
@apiParam {Number=≥1} top <mark>Giới hạn số lượng bản ghi


@apiParamExample URL request:
{host}/api/v1.0/customers/10/history-buys?sort=-buy_at&top=4


@apiSuccess {String}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin sản phẩm
@apiSuccess {Number}    O.data.product_id ID sản phẩm
@apiSuccess {String}    O.data.product_code Mã sản phẩm
@apiSuccess {String}    O.data.product_name Tên sản phẩm
@apiSuccess {String}    O.data.thumbnail_link Ảnh đại diện sản phẩm
@apiSuccess {Number}    O.data.price Giá gốc của sản phẩm
@apiSuccess {String}    O.data.unit Đơn vị của sản phẩm
@apiSuccess {String}    O.data.unit_child Đơn vị con của sản phẩm
@apiSuccess {Number}    O.data.quantity Số lượng của sản phẩm
@apiSuccess {Number}    O.data.quantity_child Số lượng con của sản phẩm
@apiSuccess {Date}      O.data.expired_at Ngày hết hạn
@apiSuccess {Number}    O.data.guarantee Bảo hành
@apiSuccess {Number}    O.data.quantity_sold Số lượng đã bán
@apiSuccess {Number}    O.data.views Số lượt xem
@apiSuccess {Number}    O.data.max_buy_number Số lượng mua tối đa
@apiSuccess {Number}    O.data.sale_price Giá bán khuyễn mãi
@apiSuccess {Number}    O.data.sale_percent Phần trăm khuyến mãi
@apiSuccess {Number}    O.data.hot Sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.new Sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.special Sản phẩm đặc biệt
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Object}    O.data.promotion Thông tin khuyến mãi của sản phẩm
@apiSuccess {Number}    O.data.promotion.promotion_id ID khuyến mãi
@apiSuccess {String}    O.data.promotion.promotion_code Mã khuyến mãi
@apiSuccess {String}    O.data.promotion.promotion_name Tên khuyến mãi
@apiSuccess {String}    O.data.promotion.content Nội dung khuyến mãi
@apiSuccess {String}    O.data.promotion.image_link Ảnh khuyến mãi

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách sản phẩm khách hàng đã mua thành công!",
    "data": [
        {
            "product_id": 1,
            "product_code": "SP0001"
            "product_name": "Sản phẩm 1"
            "thumbnail_link": "thumbnail.png"
            "price": 30000,
            "unit": "Thùng",
            "unit_child": "Chai",
            "quantity": 9999,
            "quantity_child": 24,
            "expired_at": "01/01/2023",
            "guarantee": 6,
            "quantity_sold": 9999,
            "views": 10000,
            "max_buy_number": 50,
            "sale_price": 15000,
            "sale_percent": 50,
            "hot": 0,
            "new": 0,
            "promotion": {
                "promotion_id": 1,
                "promotion_code": "KM00050",
                "promotion_name": "Khuyến mãi",
                "content": "Khuyến mãi tất cả sản phẩm ngày hôm nay",
                "image_link": "image.jpg"
            }
        },
        {
            "product_id": 2,
            "product_code": "SP0002"
            "product_name": "Sản phẩm 2"
            "thumbnail_link": "thumbnail.png"
            "price": 30000,
            "unit": "Thùng",
            "unit_child": "Gói",
            "quantity": 9999,
            "quantity_child": 30,
            "expired_at": "01/01/2023",
            "guarantee": 3,
            "quantity_sold": 8798,
            "views": 454,
            "max_buy_number": 50,
            "sale_price": 0,
            "sale_percent": 0,
            "hot": 0,
            "new": 0,
            "promotion": null
        },
        {
            "product_id": 3,
            "product_code": "SP0003"
            "product_name": "Sản phẩm 3"
            "thumbnail_link": "thumbnail.png"
            "price": 30000,
            "unit": "Thùng",
            "unit_child": "Hộp",
            "quantity": 9999,
            "quantity_child": 10,
            "expired_at": "01/01/2023",
            "guarantee": 8,
            "quantity_sold": 564,
            "views": 5456,
            "max_buy_number": 50,
            "sale_price": 15000,
            "sale_percent": 50,
            "hot": 0,
            "new": 0,
            "promotion": {
                "promotion_id": 1,
                "promotion_code": "KM00010",
                "promotion_name": "Khuyến mãi 10",
                "content": "Khuyến mãi tất cả sản phẩm sữa",
                "image_link": "image.jpg"
            }
        },
        {
            "product__id": 4,
            "product_code": "SP0004"
            "product_name": "Sản phẩm 4"
            "thumbnail_link": "thumbnail.png"
            "price": 30000,
            "unit": "Lốc",
            "unit_child": "Chai",
            "quantity": 9999,
            "quantity_child": 6,
            "expired_at": "01/01/2023",
            "guarantee": 12,
            "quantity_sold": 67,
            "views": 6767,
            "max_buy_number": 50,
            "sale_price": 0,
            "sale_percent": 0,
            "hot": 0,
            "new": 0
            "promotion": null
        }
    ]
}

@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Không tìm thấy dữ liệu.
<ul>
    <li><code>code:</code> 404</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 400:
{
    "code": 400,
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 404:
{
    "code": 404,
    "message": "Không tìm thấy dữ liệu!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi lấy lịch sử tìm kiếm: Mô tả lỗi."
}
"""