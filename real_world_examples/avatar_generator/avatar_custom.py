import py_avataaars as pa

avatar = pa.PyAvataaar(
    style=pa.AvatarStyle.TRANSPARENT,
    skin_color=pa.SkinColor.LIGHT,
    hair_color=pa.HairColor.BLACK,
    facial_hair_type=pa.FacialHairType.DEFAULT,
    facial_hair_color=pa.HairColor.BLACK,
    top_type=pa.TopType.SHORT_HAIR_SHORT_FLAT,
    hat_color=pa.Color.BLACK,
    mouth_type=pa.MouthType.SMILE,
    eye_type=pa.EyesType.DEFAULT,
    eyebrow_type=pa.EyebrowType.DEFAULT,
    nose_type=pa.NoseType.DEFAULT,
    accessories_type=pa.AccessoriesType.SUNGLASSES,
    clothe_type=pa.ClotheType.SHIRT_V_NECK,
    clothe_color=pa.Color.BLUE_03,
    clothe_graphic_type=pa.ClotheGraphicType.BAT,
)
avatar.render_png_file('avatar_custom.png')
