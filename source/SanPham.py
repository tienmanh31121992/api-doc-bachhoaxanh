"""
    @api {get} /danh-muc-san-pham Lấy danh mục sản phẩm
    @apiName Lấy_danh_mục_sản_phẩm
    @apiGroup Sản_phẩm
    @apiVersion  1.0.0
    @apiDescription Lấy danh mục sản phẩm cho Menu hiển thị


    @apiParam {Number[]} level Danh sách "cấp bậc" của nhóm sản phẩm

    @apiParamExample {JSON} Dữ liệu mẫu:
    {
        "level": [1,2]
    }


    @apiSuccess (Thành công 200) {Object} Object Kết quả trả về 
    @apiSuccess (Thành công 200) {String} Object.code Mã trạng thái HTTP
    @apiSuccess (Thành công 200) {String} Object.message Thông báo kết quả
    @apiSuccess (Thành công 200) {Object[]} Object.data Danh sách đối tượng nhóm sản phẩm
    @apiSuccess (Thành công 200) {Number} Object.data.id ID nhóm sản phẩm
    @apiSuccess (Thành công 200) {Number} Object.data.id_cha ID nhóm sản phẩm cha
    @apiSuccess (Thành công 200) {String} Object.data.ma_nhom_san_pham Mã nhóm sản phẩm
    @apiSuccess (Thành công 200) {String} Object.data.ten_nhom_san_pham Tên nhóm sản phẩm
    @apiSuccess (Thành công 200) {Number} Object.data.new Nhóm sản phẩm mới (0: False, 1: True)
    @apiSuccess (Thành công 200) {Number} Object.data.level Cấp nhóm sản phẩm
    @apiSuccess (Thành công 200) {Object[]} Object.data.nhom_san_pham_con Danh sách đối tượng nhóm sản phẩm
    @apiSuccess (Thành công 200) {Number} Object.data.nhom_san_pham_con.id ID nhóm sản phẩm
    @apiSuccess (Thành công 200) {Number} Object.data.nhom_san_pham_con.id_cha ID nhóm sản phẩm cha
    @apiSuccess (Thành công 200) {String} Object.data.nhom_san_pham_con.ma_nhom_san_pham Mã nhóm sản phẩm
    @apiSuccess (Thành công 200) {String} Object.data.nhom_san_pham_con.ten_nhom_san_pham Tên nhóm sản phẩm
    @apiSuccess (Thành công 200) {Number} Object.data.nhom_san_pham_con.new Nhóm sản phẩm mới (0: False, 1: True)
    @apiSuccess (Thành công 200) {Number} Object.data.nhom_san_pham_con.level Cấp nhóm sản phẩm

    @apiSuccessExample {JSON} Lấy danh mục sản phẩm thành công:
    {
        "code": 200,
        "message": "Lấy danh mục sản phẩm thành công!",
        "data": [
            {
                "id": 1,
                "id_cha": null,
                "ma_nhom_san_pham": "NSP0001",
                "ten_nhom_san_pham": "Thịt, cá, trúng, rau",
                "new": 1,
                "level": 1,
                "nhom_san_pham_con": [
                    {
                        "id": 2,
                        "id_cha": 1,
                        "ma_nhom_san_pham": "NSP0002",
                        "ten_nhom_san_pham": "Trái cây tươi ngon",
                        "new": 0,
                        "level": 2
                    },
                    {
                        "id": 5,
                        "id_cha": 1,
                        "ma_nhom_san_pham": "NSP0005",
                        "ten_nhom_san_pham": "Thực phẩm sơ chế",
                        "new": 0,
                        "level": 2
                    }
                ]
            },
            {
                "id": 3,
                "id_cha": null,
                "ma_nhom_san_pham": "NSP0003",
                "ten_nhom_san_pham": "Đồ uống các loại",
                "new": 0,
                "level": 1,
                "nhom_san_pham_con": [
                    {
                        "id": 4,
                        "id_cha": 3,
                        "ma_nhom_san_pham": "NSP0004",
                        "ten_nhom_san_pham": "Nước ngọt nước trà",
                        "new": 0,
                        "level": 2
                    }
                ]
            }
        ]
    }
   

    @apiError (Thất bại 400/500) {Object} Object Kết quả trả về 
    @apiError (Thất bại 400/500) {String} Object.code Mã trạng thái HTTP
    @apiError (Thất bại 400/500) {String} Object.message Thông báo kết quả

    @apiErrorExample {JSON} Lấy danh mục sản phầm thất bại:
    {
        "code": 400,
        "message": "Lấy danh mục sản phầm thất bại!"
    }

    @apiErrorExample {JSON} Lỗi hệ thống:
    {
        "code": 500,
        "message": "Xảy ra lỗi khi lấy danh mục sản phẩm!"
    }
"""

"""
    @api {get} /nhom-san-pham?hot=hot&top=top Lấy danh sách nhóm hàng thường mua
    @apiName Lấy_danh_sách_nhóm_hàng_hot
    @apiGroup Sản_phẩm
    @apiVersion  1.0.0


    @apiParam  {Number} hot Chọn loại nhóm hàng "hot" cần lấy (0: False, 1: True)
    @apiParam  {Number} top Số lượng nhóm sản phẩm cần lấy

    @apiParamExample Ví dụ sử dụng:
    https://www.bachhoaxanh.com/nhom-san-pham?hot=1&top=2


    @apiSuccess (Thành công 200) {Object} Object Kết quả trả về 
    @apiSuccess (Thành công 200) {String} Object.code Mã trạng thái HTTP
    @apiSuccess (Thành công 200) {String} Object.message Thông báo kết quả
    @apiSuccess (Thành công 200) {Object[]} Object.data Danh sách đối tượng nhóm sản phẩm
    @apiSuccess (Thành công 200) {Number} Object.data.id ID nhóm sản phẩm
    @apiSuccess (Thành công 200) {String} Object.data.ma_nhom_san_pham Mã nhóm sản phẩm
    @apiSuccess (Thành công 200) {String} Object.data.ten_nhom_san_pham Tên nhóm sản phẩm
    @apiSuccess (Thành công 200) {String} Object.data.link_icon Đường dẫn lưu icon nhóm sản phẩm

    @apiSuccessExample {JSON} Lấy danh sách nhóm hàng hot thành công:
    {
        "code": 200,
        "message": "Lấy danh sách nhóm hàng thường mua thành công!",
        "data": [
            {
                "id": 1,
                "ma_nhom_san_pham": "NSP0001",
                "ten_nhom_san_pham": "Thịt, cá, trúng, rau",
                "link_icon": "icon1.png",
            },
            {
                "id": 10,
                "ma_nhom_san_pham": "NSP0010",
                "ten_nhom_san_pham": "Sữa tươi các loại",
                "link_icon": "icon1.png",
            }
        ]
    }


    @apiError (Thất bại 400/500) {Object} Object Kết quả trả về 
    @apiError (Thất bại 400/500) {String} Object.code Mã trạng thái HTTP
    @apiError (Thất bại 400/500) {String} Object.message Thông báo kết quả

    @apiErrorExample {JSON} Lấy danh sách nhóm hàng hot thất bại:
    {
        "code": 400,
        "message": "Lấy danh sách nhóm hàng hot thất bại!"
    }

    @apiErrorExample {JSON} Lỗi hệ thống:
    {
        "code": 500,
        "message": "Xảy ra lỗi khi lấy danh sách nhóm hàng hot sản phẩm!"
    }
"""

"""
    @api {get} /ds-thuong-hieu Lấy danh sách thương hiệu
    @apiName Lấy_danh_sách_thương_hiệu
    @apiGroup Sản_phẩm
    @apiVersion  1.0.0


    @apiParam (Body)  {JSON} [Object] description


    @apiParam  {String} [paramName] description <code>RED</code>
    <ul>
        <li>asdasda</li>
        <li>asdasda</li>
    </ul>

    @apiSuccess (200) {type} name description

    @apiParamExample  {type} Request-Example:
    {
        property : value
    }


    @apiSuccessExample {type} Success-Response:
    {
        property : value
    }
"""

"""
    @api {get} /ds-san-pham Lấy danh sách sản phẩm
    @apiName Lấy_danh_sách_sản_phẩm
    @apiGroup Sản_phẩm
    @apiVersion  1.0.0
   
   
    @apiParam  {String} paramName description

    @apiParamExample  {type} Request-Example:
    {
        property : value
    }
   
    @apiSuccess (200) {type} name description
   
   
   
   
    @apiSuccessExample {type} Success-Response:
    {
        property : value
    }
"""