"""
@api {get} /product-group-menu Lấy danh mục sản phẩm
@apiName Lấy_danh_mục_sản_phẩm
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy danh mục sản phẩm để hiển thị menu


@apiParam {Number} [promotion_id] <mark>ID khuyến mãi</mark>
<ul>
    <li><code>0:</code> Lấy danh mục không có khuyến mãi</li>
    <li><code>-1:</code> Lấy tất cả danh mục đang khuyến mãi</li>
</ul>

@apiParamExample {String} URL request:
https://www.bachhoaxanh.com/api/v1/product-group-menu


@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {Object[]}  data Danh sách thông tin nhóm sản phẩm
@apiSuccess {Number}    data.id ID nhóm sản phẩm
@apiSuccess {Number}    data.parent_id ID nhóm sản phẩm cha
@apiSuccess {String}    data.code Mã nhóm sản phẩm
@apiSuccess {String}    data.name Tên nhóm sản phẩm
@apiSuccess {String}    data.icon_link Đường dẫn icon nhóm sản phẩm
@apiSuccess {String}    data.content_html Nội dung mô tả nhóm sản phẩm
@apiSuccess {Number}    data.level Cấp nhóm sản phẩm
@apiSuccess {Number}    data.new Nhóm sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.hot Nhóm sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.quantity_product_promotion Số lượng sản phẩm khuyến mãi
@apiSuccess {Object[]}  data.child Danh sách thông tin nhóm sản phẩm con
@apiSuccess {Number}    data.child.id ID nhóm sản phẩm
@apiSuccess {Number}    data.child.parent_id ID nhóm sản phẩm cha
@apiSuccess {String}    data.child.code Mã nhóm sản phẩm
@apiSuccess {String}    data.child.name Tên nhóm sản phẩm
@apiSuccess {String}    data.child.icon_link Đường dẫn icon nhóm sản phẩm
@apiSuccess {String}    data.child.content_html Nội dung mô tả nhóm sản phẩm
@apiSuccess {Number}    data.child.level Cấp nhóm sản phẩm
@apiSuccess {Number}    data.child.new Nhóm sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.child.hot Nhóm sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.child.quantity_product_promotion Số lượng sản phẩm khuyến mãi

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh mục phẩm thành công!",
    "data": [
        {
            "id": 1,
            "parent_id": 0,
            "code": "NSP0001",
            "name": "Thịt, cá, trúng, rau",
            "icon_link": "icon1.png",
            "content_html": "ádasdasdasdasd",
            "level": 1,
            "new": 1,
            "hot": 1,
            "quantity_product_promotion": null,
            "child": [
                {
                    "id": 2,
                    "parent_id": 1,
                    "code": "NSP0002",
                    "name": "Trái cây tươi ngon",
                    "icon_link": "icon2.png",
                    "content_html": "ádasdasdasdasd",
                    "level": 2,
                    "new": 0,
                    "hot": 1,
                    "quantity_product_promotion": null,
                },
                {
                    "id": 5,
                    "parent_id": 1,
                    "code": "NSP0005",
                    "name": "Thực phẩm sơ chế",
                    "icon_link": "icon5.png",
                    "content_html": "ádasdasdasdasd",
                    "level": 2,
                    "new": 0,
                    "hot": 0,
                    "quantity_product_promotion": null,
                }
            ]
        },
        {
            "id": 3,
            "parent_id": 0,
            "code": "NSP0003",
            "name": "Đồ uống các loại",
            "icon_link": "icon3.png",
            "content_html": "ádasdasdasdasd",
            "level": 1,
            "new": 0,
            "hot": 0,
            "quantity_product_promotion": null,
            "child": [
                {
                    "id": 4,
                    "parent_id": 3,
                    "code": "NSP0004",
                    "name": "Nước ngọt nước trà",
                    "icon_link": "icon4.png",
                    "content_html": "ádasdasdasdasd",
                    "level": 2,
                    "new": 0,
                    "hot": 0,
                    "quantity_product_promotion": null,
                }
            ]
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
    <li><code>code:</code> 416</li>
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
    "message": "Xảy ra lỗi khi lấy danh mục sản phẩm: Mô tả lỗi."
}
"""

"""
@api {get} /product-group Lấy danh sách nhóm sản phẩm
@apiName Lấy_danh_sách_nhóm_sản_phẩm
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy danh sách nhóm sản phẩm


@apiParam {Number} [keyword] <mark>Từ khóa tìm kiếm</mark>
@apiParam {Number} [parent_id] <mark>ID nhóm sản phẩm cha</mark>
@apiParam {Number} [hot] <mark>Nhóm sản phẩm hot</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiParam {Number} [new] <mark>Nhóm sản phẩm mới</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiParam {Number} [promotion_id] <mark>ID khuyến mãi</mark>
<ul>
    <li><code>0:</code> Lấy nhóm sản phẩm không có khuyến mãi</li>
    <li><code>-1:</code> Lấy tất cả nhóm sản phẩm đang khuyến mãi</li>
</ul>
@apiParam {String} sort_by <mark>Sắp xếp theo: Mặc định là id</mark>
@apiParam {String} sort_order <mark>Kiểu sắp xếp: Mặc định asc</mark>
@apiParam {Number} [limit] <mark>Giới hạn số lượng bản ghi</mark>
@apiParam {Number} [offset] <mark>Số phần tử bỏ qua</mark>

@apiParamExample URL request:
https://www.bachhoaxanh.com/api/v1/product-group?hot=1&sort_by=id&sort_order=asc&limit=10


@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {Object[]}  data Danh sách thông tin nhóm sản phẩm
@apiSuccess {Number}    data.id ID nhóm sản phẩm
@apiSuccess {Number}    data.parent_id ID nhóm sản phẩm cha
@apiSuccess {String}    data.code Mã nhóm sản phẩm
@apiSuccess {String}    data.name Tên nhóm sản phẩm
@apiSuccess {String}    data.icon_link Đường dẫn icon nhóm sản phẩm
@apiSuccess {String}    data.content_html Nội dung mô tả nhóm sản phẩm
@apiSuccess {Number}    data.level Cấp nhóm sản phẩm
@apiSuccess {Number}    data.new Nhóm sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.hot Nhóm sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách nhóm sản phẩm thành công!",
    "data": [
        {
            "id": 1,
            "parent_id": null,
            "code": "NSP0001",
            "name": "Thịt, cá, trúng, rau",
            "icon_link": "icon1.png",
            "content_html": "ádasdasdasdasd",
            "level": 1,
            "new": 1,
            "hot": 1
        },
        {
            "id": 2,
            "parent_id": 1,
            "code": "NSP0002",
            "name": "Trái cây tươi ngon",
            "icon_link": "icon2.png",
            "content_html": "ádasdasdasdasd",
            "level": 2,
            "new": 0,
            "hot": 1
        },
        {
            "id": 5,
            "parent_id": 1,
            "code": "NSP0005",
            "name": "Thực phẩm sơ chế",
            "icon_link": "icon5.png",
            "content_html": "ádasdasdasdasd",
            "level": 2,
            "new": 0,
            "hot": 1
        },
        {
            "id": 3,
            "parent_id": null,
            "code": "NSP0003",
            "name": "Đồ uống các loại",
            "icon_link": "icon3.png",
            "content_html": "ádasdasdasdasd",
            "level": 1,
            "new": 0,
            "hot": 1
        },
        {
            "id": 4,
            "parent_id": 3,
            "code": "NSP0004",
            "name": "Nước ngọt nước trà",
            "icon_link": "icon4.png",
            "content_html": "ádasdasdasdasd",
            "level": 2,
            "new": 0,
            "hot": 0
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
    "message": "Xảy ra lỗi khi lấy danh sách nhóm sản phẩm: Mô tả lỗi."
}
"""

"""
@api {get} /brand Lấy danh sách thương hiệu
@apiName Lấy_danh_sách_thương_hiệu
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy danh sách thương hiệu


@apiParam {Number} [keyword] <mark>Từ khóa tìm kiếm</mark>
@apiParam {Number} [product_group_id] <mark>ID nhóm sản phẩm</mark>
@apiParam {Number} [hot] <mark>Thương hiệu hot</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiParam {Number} [new] <mark>Thương hiệu mới</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiParam {Number} [promotion_id] <mark>ID khuyến mãi</mark>
<ul>
    <li><code>0:</code> Lấy thương hiệu không có khuyến mãi</li>
    <li><code>-1:</code> Lấy tất cả thương hiệu đang khuyến mãi</li>
</ul>
@apiParam {String} sort_by <mark>Sắp xếp theo: Mặc định là id</mark>
@apiParam {String} sort_order <mark>Kiểu sắp xếp: Mặc định asc</mark>
@apiParam {Number} [limit] <mark>Giới hạn số lượng bản ghi</mark>
@apiParam {Number} [offset] <mark>Số phần tử bỏ qua</mark>

@apiParamExample URL request:
https://www.bachhoaxanh.com/api/v1/brand?product_group_id=9&sort_by=id&sort_order=asc


@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {Object[]}  data Danh sách thông tin thương hiệu
@apiSuccess {Number}    data.id ID thương hiệu
@apiSuccess {String}    data.brand_code Mã thương hiệu
@apiSuccess {String}    data.brand_name Tên thương hiệu
@apiSuccess {String}    data.logo_link Đường dẫn logo
@apiSuccess {String}    data.content_html Nội dung mô tả thương hiệu
@apiSuccess {Number}    data.new Thương hiệu mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.hot Thương hiệu hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>


@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách thương hiệu thành công!",
    "data": [
        {
            "id": 1,
            "brand_code": "VINAMILK"
            "brand_name": "Vinamilk"
            "logo_link": "vinamilk.png"
            "content_html": "fdgdfgdfgssfsdf"
            "hot": 0,
            "new": 0,
        },
        {
            "id": 2,
            "brand_code": "OMO"
            "brand_name": "OMO"
            "logo_link": "omo.png"
            "content_html": "fdgdfgdfgssfsdf"
            "hot": 0,
            "new": 0,
        },
        {
            "id": 3,
            "brand_code": "PEPSI"
            "brand_name": "Pepsi"
            "logo_link": "pepsi.png"
            "content_html": "fdgdfgdfgssfsdf"
            "hot": 0,
            "new": 0,
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
    "message": "Xảy ra lỗi khi lấy danh sách thương hiệu: Mô tả lỗi."
}
"""

"""
@api {get} /product Lấy danh sách sản phẩm
@apiName Lấy_danh_sách_sản_phẩm
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy danh sách sản phẩm


@apiParam {String} [keywork] <mark>Từ khóa tìm kiếm</mark>
@apiParam {Number} [product_group_id] <mark>ID nhóm sản phẩm</mark>
@apiParam {Number} [brand_id] <mark>ID thương hiệu</mark>
@apiParam {Number} [tag_id] <mark>ID tag</mark>
@apiParam {Number} [hot] <mark>Sản phẩm hot</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiParam {Number} [new] <mark>Sản phẩm mới</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiParam {Number} [promotion_id] <mark>ID khuyến mãi</mark>
<ul>
    <li><code>0:</code> Lấy sản phẩm không có khuyến mãi</li>
    <li><code>-1:</code> Lấy tất cả sản phẩm đang khuyến mãi</li>
</ul>
@apiParam {String} sort_by <mark>Sắp xếp theo: Mặc định là id</mark>
@apiParam {String} sort_order <mark>Kiểu sắp xếp: Mặc định asc</mark>
@apiParam {Number} limit <mark>Giới hạn số lượng bản ghi</mark>
@apiParam {Number} offset <mark>Số phần tử bỏ qua</mark>

@apiParamExample URL request:
https://www.bachhoaxanh.com/api/v1/product?product_group_id=10&brand_id=9&sort_by=id&sort_order=asc&limit=4&offset=0


@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {Object[]}  data Danh sách thông tin sản phẩm
@apiSuccess {Number}    data.id ID sản phẩm
@apiSuccess {String}    data.product_code Mã sản phẩm
@apiSuccess {String}    data.product_name Tên sản phẩm
@apiSuccess {String}    data.thumbnail_link Ảnh đại diện sản phẩm
@apiSuccess {Number}    data.price Giá gốc của sản phẩm
@apiSuccess {String}    data.unit Đơn vị của sản phẩm
@apiSuccess {String}    data.unit_child Đơn vị con của sản phẩm
@apiSuccess {Number}    data.quantity Số lượng của sản phẩm
@apiSuccess {Number}    data.quantity_child Số lượng con trong sản phẩm
@apiSuccess {Date}      data.expired_at Ngày hết hạn
@apiSuccess {Number}    data.guarantee Bảo hành
@apiSuccess {Number}    data.quantity_sold Số lượng đã bán
@apiSuccess {Number}    data.views Số lượt xem
@apiSuccess {Number}    data.max_buy_number Số lượng mua tối đa
@apiSuccess {Number}    data.sale_price Giá bán khuyễn mãi
@apiSuccess {Number}    data.sale_percent Phần trăm khuyến mãi
@apiSuccess {Number}    data.new Sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.hot Sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.special Sản phẩm đặc biệt
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess             data.promotion Thông tin khuyến mãi của sản phẩm
@apiSuccess {Number}    data.promotion.id ID khuyến mãi
@apiSuccess {String}    data.promotion.promotion_code Mã khuyến mãi
@apiSuccess {String}    data.promotion.promotion_name Tên khuyến mãi
@apiSuccess {String}    data.promotion.content Nội dung khuyến mãi
@apiSuccess {String}    data.promotion.image_link Ảnh khuyến mãi

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách sản phẩm thành công!",
    "data": [
        {
            "id": 1,
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
                "id": 1,
                "promotion_code": "KM00050",
                "promotion_name": "Khuyến mãi",
                "content": "Khuyến mãi tất cả sản phẩm ngày hôm nay",
                "image_link": "image.jpg"
            }
        },
        {
            "id": 2,
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
            "id": 3,
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
                "id": 1,
                "promotion_code": "KM00010",
                "promotion_name": "Khuyến mãi 10",
                "content": "Khuyến mãi tất cả sản phẩm sữa",
                "image_link": "image.jpg"
            }
        },
        {
            "id": 4,
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
    "message": "Xảy ra lỗi khi lấy danh sách sản phẩm: Mô tả lỗi."
}
"""

"""
@api {get} /product/<id> Lấy thông tin chi tiết sản phẩm
@apiName Lấy_thông_tin_sản_phẩm
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy thông tin chi tiết của sản phẩm


@apiParam (Path) {Number} id <mark>ID sản phẩm</mark>

@apiParamExample URL request:
https://www.bachhoaxanh.com/api/v1/product/10


@apiSuccess {Object}    data Thông tin chi tiết sản phẩm
@apiSuccess {Number}    data.id ID sản phẩm
@apiSuccess {String}    data.product_code Mã sản phẩm
@apiSuccess {String}    data.product_name Tên sản phẩm
@apiSuccess {String}    data.thumbnail_link Ảnh đại diện sản phẩm
@apiSuccess {Number}    data.price Giá gốc của sản phẩm
@apiSuccess {String}    data.unit Đơn vị của sản phẩm
@apiSuccess {String}    data.unit_child Đơn vị con của sản phẩm
@apiSuccess {Number}    data.quantity Số lượng của sản phẩm
@apiSuccess {Number}    data.quantity_child Số lượng con trong sản phẩm
@apiSuccess {Number}    data.guarantee Bảo hành
@apiSuccess {Date}      data.expired_at Ngày hết hạn
@apiSuccess {Number}    data.max_buy_number Số lượng mua tối đa
@apiSuccess {Number}    data.sale_price Giá bán khuyễn mãi
@apiSuccess {Number}    data.sale_percent Phần trăm khuyến mãi
@apiSuccess {Number}    data.new Sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    data.hot Sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {String}    data.info_html Thông tin sản phẩm
@apiSuccess {String}    data.note_html Ghi chú sản phẩm
@apiSuccess {Number}    data.views Số lượt xem
@apiSuccess {String}    data.warning Lưu ý về sản phẩm
@apiSuccess {Number[]}  data.tag_id Danh sách ID tag
@apiSuccess {Object}    data.promotion Thông tin khuyến mãi của sản phẩm
@apiSuccess {Number}    data.promotion.id ID khuyến mãi
@apiSuccess {String}    data.promotion.promotion_code Mã khuyến mãi
@apiSuccess {String}    data.promotion.promotion_name Tên khuyến mãi
@apiSuccess {String}    data.promotion.content Nội dung khuyến mãi
@apiSuccess {String}    data.promotion.image_link Ảnh khuyến mãi
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy thông tin sản phẩm thành công!",
    "data": {
        "id": 10,
        "product_code": "SP00010"
        "product_name": "Sản phẩm 10"
        "thumbnail_link": "thumbnail.png"
        "price": 30000,
        "unit": "Thùng",
        "unit_child": "Chai",
        "quantity": 9999,
        "quantity_child": 24,
        "guarantee": 6,
        "expired_at": "01/01/2023",
        "max_buy_number": 50,
        "sale_price": 15000,
        "sale_percent": 50,
        "hot": 0,
        "new": 0,
        "info_html": "Thông tin",
        "note_html": "Ghi chú",
        "views": 10000,
        "warning": "Lưu ý",
        "tag_id": [1,2,3],
        "promotion": {
            "id": 1,
            "promotion_code": "KM00010",
            "promotion_name": "Khuyến mãi 10",
            "content": "Khuyến mãi tất cả sản phẩm sữa",
            "image_link": "image.jpg"
        }
    }
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
    "message": "Xảy ra lỗi khi lấy thông tin sản phẩm: Mô tả lỗi."
}
"""