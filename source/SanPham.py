"""
@api {get} /productgroups/menu Lấy danh mục sản phẩm
@apiName Lấy_danh_mục_sản_phẩm
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy danh mục sản phẩm để hiển thị menu


@apiParam {Number} [promotion_id] <mark>ID khuyến mãi</mark>
<ul>
    <li><code>0:</code> Lấy tất cả danh mục menu không có sản phẩm khuyến mãi</li>
    <li><code>-1:</code> Lấy tất cả danh mục menu đang có sản phẩm khuyến mãi</li>
    <li><code>Không có:</code> Lấy cả hai</li>
    <li><code>promotion_id</code> Lấy tất cả danh mục menu có <b>ID khuyến mãi</b></li>
</ul>

@apiParamExample {String} URL request:
{host}/api/v1.0/productgroups/menu


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin nhóm sản phẩm
@apiSuccess {Number}    O.data.id ID nhóm sản phẩm
@apiSuccess {Number}    O.data.parent_id ID nhóm sản phẩm cha
@apiSuccess {String}    O.data.code Mã nhóm sản phẩm
@apiSuccess {String}    O.data.name Tên nhóm sản phẩm
@apiSuccess {String}    O.data.icon_link Đường dẫn icon nhóm sản phẩm
@apiSuccess {String}    O.data.content_html Nội dung mô tả nhóm sản phẩm
@apiSuccess {Number}    O.data.level Cấp nhóm sản phẩm
@apiSuccess {Number}    O.data.new Nhóm sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.hot Nhóm sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.number_of_product_promotion Số lượng sản phẩm khuyến mãi trong danh mục
@apiSuccess {Object[]}  O.data.child Danh sách thông tin nhóm sản phẩm con
@apiSuccess {Number}    O.data.child.id ID nhóm sản phẩm
@apiSuccess {Number}    O.data.child.parent_id ID nhóm sản phẩm cha
@apiSuccess {String}    O.data.child.code Mã nhóm sản phẩm
@apiSuccess {String}    O.data.child.name Tên nhóm sản phẩm
@apiSuccess {String}    O.data.child.icon_link Đường dẫn icon nhóm sản phẩm
@apiSuccess {String}    O.data.child.content_html Nội dung mô tả nhóm sản phẩm
@apiSuccess {Number}    O.data.child.level Cấp nhóm sản phẩm
@apiSuccess {Number}    O.data.child.new Nhóm sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.child.hot Nhóm sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.child.number_of_product_promotion Số lượng sản phẩm khuyến mãi trong danh mục

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
            "number_of_product_promotion": 25,
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
                    "number_of_product_promotion": 12,
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
                    "number_of_product_promotion": 13,
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
            "number_of_product_promotion": 30,
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
                    "number_of_product_promotion": 30,
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
@api {get} /productgroups Lấy danh sách nhóm sản phẩm
@apiName Lấy_danh_sách_nhóm_sản_phẩm
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy danh sách nhóm sản phẩm


@apiParam {String} [keyword] <mark>Từ khóa tìm kiếm</mark>
@apiParam {Number} [parent_id] <mark>ID nhóm sản phẩm cha</mark>
@apiParam {Number=0,1} [hot] <mark>Nhóm sản phẩm hot</mark>
<ul>
    <li><code>0:</code> Lấy nhóm sản phẩm thường</li>
    <li><code>1:</code> Lấy nhóm sản phẩm hot</li>
    <li><code>Không có:</code> Lấy cả hai</li>
</ul>
@apiParam {Number=0,1} [new] <mark>Nhóm sản phẩm mới</mark>
<ul>
    <li><code>0:</code> Lấy nhóm sản phẩm cũ</li>
    <li><code>1:</code> Lấy nhóm sản phẩm mới</li>
    <li><code>Không có:</code> Lấy cả hai</li>
</ul>
@apiParam {Number} [promotion_id] <mark>ID khuyến mãi</mark>
<ul>
    <li><code>0:</code> Lấy tất cả nhóm sản phẩm không có sản phẩm khuyến mãi</li>
    <li><code>-1:</code> Lấy tất cả nhóm sản phẩm đang có sản phẩm khuyến mãi</li>
    <li><code>Không có:</code> Lấy cả hai</li>
    <li><code>promotion_id:</code> Lấy nhóm sản phẩm có <b>ID khuyến mãi<b></li>
</ul>
@apiParam {String=id,name,hot,new} sort=-new,+id <mark>Sắp xếp dữ liệu</mark>
<ul>
    <li><code>+:</code> Tăng dần</li>
    <li><code>-:</code> Giảm dần</li>
</ul>
@apiParam {Number=≥0} [page] <mark>Vị trí trang yêu cầu</mark>
@apiParam {Number=≥1} [per_page] <mark>Số item trên một trang</mark>

@apiParamExample URL request:
{host}/api/v1.0/productgroups?hot=1&sort=-new,+id&page=0&per_page=5


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin nhóm sản phẩm
@apiSuccess {Number}    O.data.id ID nhóm sản phẩm
@apiSuccess {Number}    O.data.parent_id ID nhóm sản phẩm cha
@apiSuccess {String}    O.data.code Mã nhóm sản phẩm
@apiSuccess {String}    O.data.name Tên nhóm sản phẩm
@apiSuccess {String}    O.data.icon_link Đường dẫn icon nhóm sản phẩm
@apiSuccess {String}    O.data.content_html Nội dung mô tả nhóm sản phẩm
@apiSuccess {Number}    O.data.level Cấp nhóm sản phẩm
@apiSuccess {Number}    O.data.new Nhóm sản phẩm mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.hot Nhóm sản phẩm hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Object}    O.paging Thông tin phân trang
@apiSuccess {Number}    O.paging.page Vị trí trang
@apiSuccess {Number}    O.paging.per_page Số phần tử trên một trang
@apiSuccess {Number}    O.paging.total_page Tổng số trang
@apiSuccess {Number}    O.paging.total_item Tổng phần tử

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách nhóm sản phẩm thành công!",
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
            "parent_id": 0,
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
    ],
    "paging": {
        "page": 0,
        "per_page": 5,
        "total_page": 11,
        "total_item": 53
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
    "message": "Xảy ra lỗi khi lấy danh sách nhóm sản phẩm: Mô tả lỗi."
}
"""

"""
@api {get} /brands Lấy danh sách thương hiệu
@apiName Lấy_danh_sách_thương_hiệu
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy danh sách thương hiệu


@apiParam {Number} [keyword] <mark>Từ khóa tìm kiếm</mark>
@apiParam {Number} [product_group_id] <mark>ID nhóm sản phẩm</mark>
@apiParam {Number=0,1} [hot] <mark>Thương hiệu hot</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
    <li><code>Không có:</code> Lấy cả hai</li>
</ul>
@apiParam {Number=0,1} [new] <mark>Thương hiệu mới</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
    <li><code>Không có:</code> Lấy cả hai</li>
</ul>
@apiParam {Number} [promotion_id] <mark>ID khuyến mãi</mark>
<ul>
    <li><code>0:</code> Lấy tất cả thương hiệu không có sản phẩm khuyến mãi</li>
    <li><code>-1:</code> Lấy tất cả thương hiệu đang có sản phẩm khuyến mãi</li>
    <li><code>Không có:</code> Lấy cả hai</li>
    <li><code>promotion_id:</code> Lấy thương hiệu có <b>ID khuyến mãi<b></li>
</ul>
@apiParam {String=id,name,hot,new} sort=+name <mark>Sắp xếp dữ liệu</mark>
<ul>
    <li><code>+:</code> Tăng dần</li>
    <li><code>-:</code> Giảm dần</li>
</ul>
@apiParam {Number=≥0} [page] <mark>Vị trí trang yêu cầu</mark>
@apiParam {Number=≥1} [per_page] <mark>Số item trên một trang</mark>

@apiParamExample URL request:
{host}/api/v1.0/brands?product_group_id=9&sort=+name&page=0&per_page=3


@apiSuccess {String}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin thương hiệu
@apiSuccess {Number}    O.data.id ID thương hiệu
@apiSuccess {String}    O.data.brand_code Mã thương hiệu
@apiSuccess {String}    O.data.brand_name Tên thương hiệu
@apiSuccess {String}    O.data.logo_link Đường dẫn logo
@apiSuccess {String}    O.data.content_html Nội dung mô tả thương hiệu
@apiSuccess {Number}    O.data.hot Thương hiệu hot
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Number}    O.data.new Thương hiệu mới
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
</ul>
@apiSuccess {Object}    O.paging Thông tin phân trang
@apiSuccess {Number}    O.paging.page Vị trí trang
@apiSuccess {Number}    O.paging.per_page Số phần tử trên một trang
@apiSuccess {Number}    O.paging.total_page Tổng số trang
@apiSuccess {Number}    O.paging.total_item Tổng phần tử


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
    ],
    "paging": {
        "page": 0,
        "per_page": 3,
        "total_page": 4,
        "total_item": 10
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
    "message": "Xảy ra lỗi khi lấy danh sách thương hiệu: Mô tả lỗi."
}
"""

"""
@api {get} /products Lấy danh sách sản phẩm
@apiName Lấy_danh_sách_sản_phẩm
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy danh sách sản phẩm


@apiParam {String} [keywork] <mark>Từ khóa tìm kiếm</mark>
@apiParam {Number} [product_group_id] <mark>ID nhóm sản phẩm</mark>
@apiParam {Number} [brand_id] <mark>ID thương hiệu</mark>
@apiParam {Number} [tag_id] <mark>ID tag</mark>
@apiParam {Number=0,1} [hot] <mark>Sản phẩm hot</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
    <li><code>Không có:</code> Lấy cả hai</li>
</ul>
@apiParam {Number=0,1} [new] <mark>Sản phẩm mới</mark>
<ul>
    <li><code>0:</code> False</li>
    <li><code>1:</code> True</li>
    <li><code>Không có:</code> Lấy cả hai</li>
</ul>
@apiParam {Number} [promotion_id] <mark>ID khuyến mãi</mark>
<ul>
    <li><code>0:</code> Lấy tất cả sản phẩm không có khuyến mãi</li>
    <li><code>-1:</code> Lấy tất cả sản phẩm đang có khuyến mãi</li>
    <li><code>Không có:</code> Lấy cả hai</li>
    <li><code>promotion_id:</code> Lấy thương hiệu có <b>ID khuyến mãi<b></li>
</ul>
@apiParam {String=id,name,hot,new} sort=+name <mark>Sắp xếp dữ liệu</mark>
<ul>
    <li><code>+:</code> Tăng dần</li>
    <li><code>-:</code> Giảm dần</li>
</ul>
@apiParam {Number=≥0} page=0 <mark>Vị trí trang yêu cầu</mark>
@apiParam {Number=≥1} per_page=1 <mark>Số item trên một trang</mark>

@apiParamExample URL request:
{host}/api/v1.0/products?product_group_id=10&brand_id=9&sort=+name&page=0&per_page=4


@apiSuccess {String}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin sản phẩm
@apiSuccess {Number}    O.data.id ID sản phẩm
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
@apiSuccess {Number}    O.data.promotion.id ID khuyến mãi
@apiSuccess {String}    O.data.promotion.promotion_code Mã khuyến mãi
@apiSuccess {String}    O.data.promotion.promotion_name Tên khuyến mãi
@apiSuccess {String}    O.data.promotion.content Nội dung khuyến mãi
@apiSuccess {String}    O.data.promotion.image_link Ảnh khuyến mãi
@apiSuccess {Object}    O.paging Thông tin phân trang
@apiSuccess {Number}    O.paging.page Vị trí trang
@apiSuccess {Number}    O.paging.per_page Số phần tử trên một trang
@apiSuccess {Number}    O.paging.total_page Tổng số trang
@apiSuccess {Number}    O.paging.total_item Tổng phần tử

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
    ],
    "paging": {
        "page": 0,
        "per_page": 4,
        "total_page": 12,
        "total_item": 45
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
    "message": "Xảy ra lỗi khi lấy danh sách sản phẩm: Mô tả lỗi."
}
"""

"""
@api {get} /products/<id> Lấy thông tin chi tiết sản phẩm
@apiName Lấy_thông_tin_sản_phẩm
@apiGroup Sản_phẩm
@apiVersion  1.0.0
@apiDescription Lấy thông tin chi tiết của sản phẩm


@apiParam (Path) {Number} id <mark>ID sản phẩm</mark>

@apiParamExample URL request:
{host}/api/v1.0/products/10


@apiSuccess {String}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object}    O.data Thông tin chi tiết sản phẩm
@apiSuccess {Number}    O.data.id ID sản phẩm
@apiSuccess {String}    O.data.product_code Mã sản phẩm
@apiSuccess {String}    O.data.product_name Tên sản phẩm
@apiSuccess {String}    O.data.thumbnail_link Ảnh đại diện sản phẩm
@apiSuccess {Number}    O.data.price Giá gốc của sản phẩm
@apiSuccess {String}    O.data.unit Đơn vị của sản phẩm
@apiSuccess {String}    O.data.unit_child Đơn vị con của sản phẩm
@apiSuccess {Number}    O.data.quantity Số lượng của sản phẩm
@apiSuccess {Number}    O.data.quantity_child Số lượng con trong sản phẩm
@apiSuccess {Number}    O.data.guarantee Bảo hành
@apiSuccess {Date}      O.data.expired_at Ngày hết hạn
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
@apiSuccess {String}    O.data.info_html Thông tin sản phẩm
@apiSuccess {String}    O.data.note_html Ghi chú sản phẩm
@apiSuccess {Number}    O.data.views Số lượt xem
@apiSuccess {String}    O.data.warning Lưu ý về sản phẩm
@apiSuccess {Number[]}  O.data.tag_id Danh sách ID tag
@apiSuccess {Object}    O.data.promotion Thông tin khuyến mãi của sản phẩm
@apiSuccess {Number}    O.data.promotion.id ID khuyến mãi
@apiSuccess {String}    O.data.promotion.promotion_code Mã khuyến mãi
@apiSuccess {String}    O.data.promotion.promotion_name Tên khuyến mãi
@apiSuccess {String}    O.data.promotion.content Nội dung khuyến mãi
@apiSuccess {String}    O.data.promotion.image_link Ảnh khuyến mãi

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


"""
@api {get} /products/historyview Lấy danh sách sản phẩm khách hàng đã xem
@apiName Sản_phẩm_đã_xem
@apiGroup Sản_phẩm
@apiVersion 1.0.0
@apiDescription Lấy danh sách sản phẩm khách hàng đã xem


@apiParam {Number} customer_id <mark>ID khách hàng</mark>
@apiParam {String=view_number,view_at} sort=-view_at <mark>Sắp xếp dữ liệu</mark>
<ul>
    <li><code>+:</code> Tăng dần</li>
    <li><code>-:</code> Giảm dần</li>
</ul>
@apiParam {Number=≥1} top <mark>Giới hạn số lượng bản ghi


@apiParamExample URL request:
{host}/api/v1.0/products/historyview?customer_id=10&sort=-view_at&top=4


@apiSuccess {String}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin sản phẩm
@apiSuccess {Number}    O.data.id ID sản phẩm
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
@apiSuccess {Number}    O.data.promotion.id ID khuyến mãi
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
    "message": "Xảy ra lỗi khi lấy lịch sử tìm kiếm: Mô tả lỗi."
}
"""

"""
@api {get} /products/historybuy Lấy danh sách sản phẩm khách hàng đã mua
@apiName Sản_phẩm_đã_mua
@apiGroup Sản_phẩm
@apiVersion 1.0.0
@apiDescription Lấy danh sách sản phẩm khách hàng đã mua


@apiParam {Number} customer_id <mark>ID khách hàng</mark>
@apiParam {String=buy_number,buy_at} sort=-buy_at <mark>Sắp xếp dữ liệu</mark>
<ul>
    <li><code>+:</code> Tăng dần</li>
    <li><code>-:</code> Giảm dần</li>
</ul>
@apiParam {Number=≥1} top <mark>Giới hạn số lượng bản ghi


@apiParamExample URL request:
{host}/api/v1.0/products/historybuy?customer_id=10&sort=-buy_at&top=4


@apiSuccess {String}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin sản phẩm
@apiSuccess {Number}    O.data.id ID sản phẩm
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
@apiSuccess {Number}    O.data.promotion.id ID khuyến mãi
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
    "message": "Xảy ra lỗi khi lấy lịch sử tìm kiếm: Mô tả lỗi."
}
"""