# <font color="azure"><div align="center"><p>**Color Mask App**</p> </div></font>

- This app, which I developed with OpenCV and PyQt5, masks the color objects in the range chosen by the user by separating them from the outside. Preferably it gives the object determination and the color numbers of the selected area. 

# <div align="center"><p>![ilk](https://github.com/furkankorlu/Color-Mask-App/assets/122547302/69b3a573-1ae8-440c-9487-08956d9e309c)</p> </div>

|<font color="White">**Package**</font>|<font color="White">**Version**</font>|
| :--------- | :-----:|
| Opencv  | 4.7.0.72 |
| Numpy|    1.19.5 |
| PyQt5 |    5.15.9 |

- The image taken from the camera is converted into HSV color space to be masked.

## <font color="HoneyDew">**HSV Colorspace**</font>

- Defines color with the terms **Hue, Saturnation** and **Value**. Spaces such as *RGB, BGR* express a mixture of colors, while *HSV* space uses color, saturation and brightness values. While saturation determines the vitality of color, brightness refers to the 	luminosity of color.

![hsvhuesaturationandvalue](https://github.com/furkankorlu/Color-Mask-App/assets/122547302/7e1df255-5340-49ff-a1b7-57ec932b9d32)

- The **lowers and upper slides** in the app allow the user to choose the *color, brightness and saturation* values that he wants to mask.

![slide](https://github.com/furkankorlu/Color-Mask-App/assets/122547302/dbc95b87-bdfe-4f99-ac26-cb45819ef3f6)


- The *HSV* range of the color to be selected can be learned from the color spectrum  available in the app or through the window that opens when the **HSV Color Detection checkbox** is checked.

![hsvtespit](https://github.com/furkankorlu/Color-Mask-App/assets/122547302/04932e02-4a6d-4a7a-a7f2-7f26c73c6ffe)


# <font color="azure"><div align="center"><p>**Color Mask App**</p> </div></font>

- OpenCV ve PyQt5 ile geliştirdiğim bu uygulama kullanıcının seçtiği aralıktaki renge sahip nesneleri dış ortamdan ayırarak maskeler. Tercihen(İsteğe bağlı) nesne tepsiti ve seçilen alanın renk numaralarını verir.

# <div align="center"><p>![ilk](https://github.com/furkankorlu/Color-Mask-App/assets/122547302/69b3a573-1ae8-440c-9487-08956d9e309c)</p> </div>

|<font color="White">**Package**</font>|<font color="White">**Version**</font>|
| :--------- | :-----:|
| Opencv  | 4.7.0.72 |
| Numpy|    1.19.5 |
| PyQt5 |    5.15.9 |
                        
- Kameradan alınan görüntü maskelenmek için HSV renk uzayına dönüştürülür. 

## <font color="HoneyDew">**HSV Renk Uzayı**</font>

- **Hue, Saturation** ve **Value** terimleri ile rengi tanımlar. *RGB, BGR* gibi uzaylar renklerin karışımını ifade ederken *HSV* uzayında renk, doygunluk ve parlaklık değerleri kullanılır. Doygunluk rengin canlılığını belirlerken parlaklık rengin aydınlığını ifade eder.

![hsvhuesaturationandvalue](https://github.com/furkankorlu/Color-Mask-App/assets/122547302/7e1df255-5340-49ff-a1b7-57ec932b9d32)

- Uygulamada bulunan **lower ve upper slidelar** kullanıcının maskelemek istediği *renk, parlaklık ve doygunluk* değerlerini seçebilmesini sağlar. 

![slide](https://github.com/furkankorlu/Color-Mask-App/assets/122547302/dbc95b87-bdfe-4f99-ac26-cb45819ef3f6)

-Seçilmek istenen rengin *HSV* aralığı uygulamada bulunan renk sprektrumundan ya da **Hsv Renk Tespit checkbox’ı** işaretlendiğinde açılan pencereden öğrenilebilir.

![hsvtespit](https://github.com/furkankorlu/Color-Mask-App/assets/122547302/04932e02-4a6d-4a7a-a7f2-7f26c73c6ffe)
