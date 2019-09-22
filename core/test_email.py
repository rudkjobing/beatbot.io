from django.core.mail import send_mail
from django.test import TestCase, override_settings


class TestEmail(TestCase):

    @override_settings(EMAIL_BACKEND="anymail.backends.sendinblue.EmailBackend")
    def test_mail(self):

        send_mail("Hello from the beatbot", "New gigs inc!", "noreply@beatbot.io",
                  ["slyngel@gmail.com"], html_message=test_text)


test_text = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta name="viewport" content="width=device-width, initial-scale=1" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="x-apple-disable-message-reformatting" /><meta name="apple-mobile-web-app-capable" content="yes" /><meta name="apple-mobile-web-app-status-bar-style" content="black" /><meta name="format-detection" content="telephone=no" /><title></title><style type="text/css">
        /* Resets */
        .ReadMsgBody { width: 100%; background-color: #ebebeb;}
        .ExternalClass {width: 100%; background-color: #ebebeb;}
        .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {line-height:100%;}
        a[x-apple-data-detectors]{
            color:inherit !important;
            text-decoration:none !important;
            font-size:inherit !important;
            font-family:inherit !important;
            font-weight:inherit !important;
            line-height:inherit !important;
        }        
        body {-webkit-text-size-adjust:none; -ms-text-size-adjust:none;}
        body {margin:0; padding:0;}
        .yshortcuts a {border-bottom: none !important;}
        .rnb-del-min-width{ min-width: 0 !important; }

        /* Add new outlook css start */
        .templateContainer{
            max-width:590px !important;
            width:auto !important;
        }
        /* Add new outlook css end */

        /* Image width by default for 3 columns */
        img[class="rnb-col-3-img"] {
        max-width:170px;
        }

        /* Image width by default for 2 columns */
        img[class="rnb-col-2-img"] {
        max-width:264px;
        }

        /* Image width by default for 2 columns aside small size */
        img[class="rnb-col-2-img-side-xs"] {
        max-width:180px;
        }

        /* Image width by default for 2 columns aside big size */
        img[class="rnb-col-2-img-side-xl"] {
        max-width:350px;
        }

        /* Image width by default for 1 column */
        img[class="rnb-col-1-img"] {
        max-width:550px;
        }

        /* Image width by default for header */
        img[class="rnb-header-img"] {
        max-width:590px;
        }

        /* Ckeditor line-height spacing */
        .rnb-force-col p, ul, ol{margin:0px!important;}
        .rnb-del-min-width p, ul, ol{margin:0px!important;}

        /* tmpl-2 preview */
        .rnb-tmpl-width{ width:100%!important;}

        /* tmpl-11 preview */
        .rnb-social-width{padding-right:15px!important;}

        /* tmpl-11 preview */
        .rnb-social-align{float:right!important;}

        /* Ul Li outlook extra spacing fix */
        li{mso-margin-top-alt: 0; mso-margin-bottom-alt: 0;}        

        /* Outlook fix */
        table {mso-table-lspace:0pt; mso-table-rspace:0pt;}
    
        /* Outlook fix */
        table, tr, td {border-collapse: collapse;}

        /* Outlook fix */
        p,a,li,blockquote {mso-line-height-rule:exactly;} 

        /* Outlook fix */
        .msib-right-img { mso-padding-alt: 0 !important;}

        /* Fix text line height on preview */ 
        .content-spacing div {display: list-item; list-style-type: none;}

        @media only screen and (min-width:590px){
        /* mac fix width */
        .templateContainer{width:590px !important;}
        }

        @media screen and (max-width: 360px){
        /* yahoo app fix width "tmpl-2 tmpl-10 tmpl-13" in android devices */
        .rnb-yahoo-width{ width:360px !important;}
        }

        @media screen and (max-width: 380px){
        /* fix width and font size "tmpl-4 tmpl-6" in mobile preview */
        .element-img-text{ font-size:24px !important;}
        .element-img-text2{ width:230px !important;}
        .content-img-text-tmpl-6{ font-size:24px !important;}
        .content-img-text2-tmpl-6{ width:220px !important;}
        }

        @media screen and (max-width: 480px) {
        td[class="rnb-container-padding"] {
        padding-left: 10px !important;
        padding-right: 10px !important;
        }

        /* force container nav to (horizontal) blocks */
        td.rnb-force-nav {
        display: inherit;
        }
        }

        @media only screen and (max-width: 600px) {

        /* center the address &amp; social icons */
        .rnb-text-center {text-align:center !important;}

        /* force container columns to (horizontal) blocks */
        td.rnb-force-col {
        display: block;
        padding-right: 0 !important;
        padding-left: 0 !important;
        width:100%;
        }

        table.rnb-container {
         width: 100% !important;
        }

        table.rnb-btn-col-content {
        width: 100% !important;
        }
        table.rnb-col-3 {
        /* unset table align="left/right" */
        float: none !important;
        width: 100% !important;

        /* change left/right padding and margins to top/bottom ones */
        margin-bottom: 10px;
        padding-bottom: 10px;
        /*border-bottom: 1px solid #eee;*/
        }

        table.rnb-last-col-3 {
        /* unset table align="left/right" */
        float: none !important;
        width: 100% !important;
        }

        table[class~="rnb-col-2"] {
        /* unset table align="left/right" */
        float: none !important;
        width: 100% !important;

        /* change left/right padding and margins to top/bottom ones */
        margin-bottom: 10px;
        padding-bottom: 10px;
        /*border-bottom: 1px solid #eee;*/
        }

        table.rnb-col-2-noborder-onright {
        /* unset table align="left/right" */
        float: none !important;
        width: 100% !important;

        /* change left/right padding and margins to top/bottom ones */
        margin-bottom: 10px;
        padding-bottom: 10px;
        }

        table.rnb-col-2-noborder-onleft {
        /* unset table align="left/right" */
        float: none !important;
        width: 100% !important;

        /* change left/right padding and margins to top/bottom ones */
        margin-top: 10px;
        padding-top: 10px;
        }

        table.rnb-last-col-2 {
        /* unset table align="left/right" */
        float: none !important;
        width: 100% !important;
        }

        table.rnb-col-1 {
        /* unset table align="left/right" */
        float: none !important;
        width: 100% !important;
        }

        img.rnb-col-3-img {
        /**max-width:none !important;**/
        width:100% !important;
        }

        img.rnb-col-2-img {
        /**max-width:none !important;**/
        width:100% !important;
        }

        img.rnb-col-2-img-side-xs {
        /**max-width:none !important;**/
        width:100% !important;
        }

        img.rnb-col-2-img-side-xl {
        /**max-width:none !important;**/
        width:100% !important;
        }

        img.rnb-col-1-img {
        /**max-width:none !important;**/
        width:100% !important;
        }

        img.rnb-header-img {
        /**max-width:none !important;**/
        width:100% !important;
        margin:0 auto;
        }

        img.rnb-logo-img {
        /**max-width:none !important;**/
        width:100% !important;
        }

        td.rnb-mbl-float-none {
        float:inherit !important;
        }

        .img-block-center{text-align:center !important;}

        .logo-img-center
        {
            float:inherit !important;
        }

        /* tmpl-11 preview */
        .rnb-social-align{margin:0 auto !important; float:inherit !important;}

        /* tmpl-11 preview */
        .rnb-social-center{display:inline-block;}

        /* tmpl-11 preview */
        .social-text-spacing{margin-bottom:0px !important; padding-bottom:0px !important;}

        /* tmpl-11 preview */
        .social-text-spacing2{padding-top:15px !important;}

    }</style><!--[if gte mso 11]><style type="text/css">table{border-spacing: 0; }table td {border-collapse: separate;}</style><![endif]--><!--[if !mso]><!--><style type="text/css">table{border-spacing: 0;} table td {border-collapse: collapse;}</style> <!--<![endif]--><!--[if gte mso 15]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]--><!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]--></head><body>

<table border="0" align="center" width="100%" cellpadding="0" cellspacing="0" class="main-template" bgcolor="#f9fafc" style="background-color: rgb(249, 250, 252);">

    <tbody><tr style="display:none !important; font-size:1px; mso-hide: all;"><td></td><td></td></tr><tr>
        <td align="center" valign="top">
        <!--[if gte mso 9]>
                        <table align="center" border="0" cellspacing="0" cellpadding="0" width="590" style="width:590px;">
                        <tr>
                        <td align="center" valign="top" width="590" style="width:590px;">
                        <![endif]-->
            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer" style="max-width:590px!important; width: 590px;">
        <tbody><tr>

        <td align="center" valign="top">

            <table class="rnb-del-min-width" width="100%" cellpadding="0" border="0" cellspacing="0" style="min-width:590px;" name="Layout_0" id="Layout_0">
                <tbody><tr>
                    <td class="rnb-del-min-width" valign="top" align="center" style="min-width:590px;">
                        <table width="100%" cellpadding="0" border="0" height="38" cellspacing="0">
                            <tbody><tr>
                                <td valign="top" height="38">
                                    <img width="20" height="38" style="display:block; max-height:38px; max-width:20px;" alt="" src="http://img.mailinblue.com/new_images/rnb/rnb_space.gif">
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody></table>
            </td>
    </tr><tr>

        <td align="center" valign="top">

            <div style="background-color: rgb(255, 255, 255); border-radius: 0px;">
                
                <!--[if mso]>
                <table align="center" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                <tr>
                <![endif]-->
                
                <!--[if mso]>
                <td valign="top" width="590" style="width:590px;">
                <![endif]-->
            
                <table width="100%" cellpadding="0" border="0" cellspacing="0" name="Layout_" id="Layout_"><tbody><tr>
                    <td align="center" valign="top"><table border="0" width="100%" cellpadding="0" cellspacing="0" class="rnb-container" bgcolor="#ffffff" style="height: 0px; background-color: rgb(255, 255, 255); border-radius: 0px; border-collapse: separate; padding-left: 20px; padding-right: 20px;"><tbody><tr>
                                <td class="rnb-container-padding" style="font-size: px;font-family: ; color: ;">

                                    <table border="0" cellpadding="0" cellspacing="0" class="rnb-columns-container" align="center" style="margin:auto;">
                                        <tbody><tr>

                                            <td class="rnb-force-col" align="center">

                                                <table border="0" cellspacing="0" cellpadding="0" align="center" class="rnb-col-1">

                                                    <tbody><tr>
                                                        <td height="10"></td>
                                                    </tr>

                                                    <tr>
                                                        <td class="content-spacing" style="font-family:Arial,Helvetica,sans-serif; color:#3c4858; text-align:center;">

                                                            <span style="color:#3c4858;"><strong><span style="font-size:24px;">Nye Konserter i Aarhus</span></strong></span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td height="10"></td>
                                                    </tr>
                                                    </tbody></table>
                                                </td></tr>
                                    </tbody></table></td>
                            </tr>

                        </tbody></table>

                    </td>
                </tr>

            </tbody></table><!--[if mso]>
                </td>
                <![endif]-->
                
                <!--[if mso]>
                </tr>
                </table>
                <![endif]-->
            
        </div></td>
    </tr><tr>

        <td align="center" valign="top">

            <div style="background-color: rgb(255, 255, 255); border-radius: 0px;">
                
                <!--[if mso]>
                <table align="center" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
                <tr>
                <![endif]-->
                
                <!--[if mso]>
                <td valign="top" width="590" style="width:590px;">
                <![endif]-->
                <table class="rnb-del-min-width" width="100%" cellpadding="0" border="0" cellspacing="0" style="min-width:100%;" name="Layout_" id="Layout_">
                <tbody><tr>
                    <td class="rnb-del-min-width" align="center" valign="top">
                        <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-container" bgcolor="#ffffff" style="max-width: 100%; min-width: 100%; table-layout: fixed; background-color: rgb(255, 255, 255); border-radius: 0px; border-collapse: separate; padding-left: 20px; padding-right: 20px;">
                            <tbody><tr>
                                <td height="20" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                            </tr>
                            <tr>
                                <td valign="top" class="rnb-container-padding" align="left">

                                    <table width="100%" border="0" cellpadding="0" cellspacing="0" class="rnb-columns-container">
                                        <tbody><tr>
                                            <td class="rnb-force-col" width="264" valign="top" style="padding-right: 20px;">
                                                <table border="0" valign="top" cellspacing="0" cellpadding="0" align="left" class="rnb-col-2" width="264">
                                                    <tbody><tr>
                                                        <td style="font-size:24px; font-family:Arial,Helvetica,sans-serif; color:#3c4858; text-align:left;">
                                                            <span style="color:#3c4858; "><strong><span style="font-size:18px;">Sorten muld</span></strong></span></td>
                                                    </tr><tr>
                                                        <td height="10" class="col_td_gap" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                                    </tr><tr>
                                                        <td style="font-size:14px; font-family:Arial,Helvetica,sans-serif, sans-serif; color:#3c4858; line-height: 21px;">
                                                            <div>Lorem ipsum dolor <a href="#" style="text-decoration: underline; color: rgb(0, 146, 255);">sit amet,consectetur adipisicing</a> elit, sed do incididunt utlabore etdolore magna aliqua. Ut enim minim.</div>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td height="10" class="col_td_gap" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                                    </tr><tr>
                                                        <td valign="top">
                                                            <table cellpadding="0" border="0" align="left" cellspacing="0" class="rnb-btn-col-content" style="border-collapse: separate;margin:0 auto;">
                                                                <tbody><tr>
                                                                    <td width="auto" valign="middle" bgcolor="#0092ff" align="left" height="32" style="font-size:14px; font-family:Arial,Helvetica,sans-serif; text-align:center; color:#ffffff; font-weight:normal; padding-left:18px; padding-right:18px; background-color:#0092ff; border-radius:4px;border-top:0px None #000;border-right:0px None #000;border-bottom:0px None #000;border-left:0px None #000;">
                                                                        <span style="color:#ffffff; font-weight:normal;">
                                                                            <a style="text-decoration:none; color:#ffffff; font-weight:normal;" target="_blank" href="http://www.beatbot.io">Button</a>
                                                                        </span>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table>
                                                        </td>
                                                        <!--[if gte mso 9]><span style="font-size:0px;line-height:0px; mso-hide: all;">&nbsp;</span><![endif]-->
                                                    </tr></tbody></table>

                                                </td><td class="rnb-force-col" width="264" valign="top" style="padding-right: 0px;">
                                                <table border="0" valign="top" cellspacing="0" cellpadding="0" align="left" class="rnb-last-col-2" width="264">
                                                    <tbody><tr>
                                                        <td style="font-size:24px; font-family:Arial,Helvetica,sans-serif; color:#3c4858; text-align:left;">
                                                            <span style="color:#3c4858; "><strong><span style="font-size:18px;">Hastesager</span></strong></span></td>
                                                    </tr><tr>
                                                        <td height="10" class="col_td_gap" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                                    </tr><tr>
                                                        <td style="font-size:14px; font-family:Arial,Helvetica,sans-serif, sans-serif; color:#3c4858; line-height: 21px;">
                                                            <div>Lorem ipsum dolor <a href="#" style="text-decoration: underline; color: rgb(0, 146, 255);">sit amet,consectetur adipisicing</a> elit, sed do incididunt utlabore etdolore magna aliqua. Ut enim minim.</div>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td height="10" class="col_td_gap" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                                    </tr><tr>
                                                        <td valign="top">
                                                            <table cellpadding="0" border="0" align="left" cellspacing="0" class="rnb-btn-col-content" style="border-collapse: separate;margin:0 auto;">
                                                                <tbody><tr>
                                                                    <td width="auto" valign="middle" bgcolor="#0092ff" align="left" height="32" style="font-size:14px; font-family:Arial,Helvetica,sans-serif; text-align:center; color:#ffffff; font-weight:normal; padding-left:18px; padding-right:18px; background-color:#0092ff; border-radius:4px;border-top:0px None #000;border-right:0px None #000;border-bottom:0px None #000;border-left:0px None #000;">
                                                                        <span style="color:#ffffff; font-weight:normal;">
                                                                            <a style="text-decoration:none; color:#ffffff; font-weight:normal;" target="_blank">Button</a>
                                                                        </span>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table>
                                                        </td>
                                                        <!--[if gte mso 9]><span style="font-size:0px;line-height:0px; mso-hide: all;">&nbsp;</span><![endif]-->
                                                    </tr></tbody></table>

                                                </td></tr>
                                    </tbody></table></td>
                            </tr>
                            <tr>
                                <td height="20" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                            </tr>
                        </tbody></table>

                    </td>
                </tr>
            </tbody></table><!--[if mso]>
                </td>
                <![endif]-->
                
                <!--[if mso]>
                </tr>
                </table>
                <![endif]-->
                
            </div></td>
    </tr><tr>

        <td align="center" valign="top">

            <table class="rnb-del-min-width" width="100%" cellpadding="0" border="0" cellspacing="0" style="min-width:590px;" name="Layout_" id="Layout_">
                <tbody><tr>
                    <td class="rnb-del-min-width" valign="top" align="center" style="min-width:590px;">
                        <table width="100%" cellpadding="0" border="0" height="30" cellspacing="0">
                            <tbody><tr>
                                <td valign="top" height="30">
                                    <img width="20" height="30" style="display:block; max-height:30px; max-width:20px;" alt="" src="http://img.mailinblue.com/new_images/rnb/rnb_space.gif">
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody></table>
            </td>
    </tr><tr>

        <td align="center" valign="top">

            <div style="background-color: rgb(249, 250, 252);">
                
                <table class="rnb-del-min-width rnb-tmpl-width" width="100%" cellpadding="0" border="0" cellspacing="0" style="min-width:590px;" name="Layout_3" id="Layout_3">
                    <tbody><tr>
                        <td class="rnb-del-min-width" align="center" valign="top" bgcolor="#f9fafc" style="min-width:590px; background-color: #f9fafc; text-align: center;">
                            <table width="590" class="rnb-container" cellpadding="0" border="0" align="center" cellspacing="0" bgcolor="#f9fafc" style="padding-right: 20px; padding-left: 20px; background-color: rgb(249, 250, 252);">
                                <tbody><tr>
                                    <td height="10" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td>
                                        <div style="font-size:14px; color:#888888; font-weight:normal; text-align:center; font-family:Arial,Helvetica,sans-serif;">This email was sent to {{ contact.EMAIL }}<div>You received this email because you are registered with Beatbot.io</div><div>&nbsp;</div></div>
                                        <div style="display: block; text-align: center;">
                                            <span style="font-size:14px; font-weight:normal; display: inline-block; text-align:center; font-family:Arial,Helvetica,sans-serif;">
                                                <a style="text-decoration:underline; color:#666666;font-size:14px;font-weight:normal;font-family:Arial,Helvetica,sans-serif;" target="_blank" href="{{ unsubscribe }}">Unsubscribe here</a></span>
                                        </div>
                                    </td></tr>
                                <tr>
                                    <td height="10" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td>
                                        <div style="text-align:center;">
                                            <a href="https://www.sendinblue.com/?utm_source=logo_mailin&amp;utm_campaign=14c9c680b61b8aa0f591a51367eabf9b&amp;utm_medium=email" target="_blank"><img border="0" hspace="0" vspace="0" width="129" height="48" alt="SendinBlue" style="margin:auto;" src="http://img.mailinblue.com/new_images/rnb/en.png"></a>
                                        </div></td>
                                </tr><tr>
                                    <td height="10" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                </tr></tbody></table>
                        </td>
                    </tr>
                </tbody></table>
                
            </div></td>
    </tr><tr>

        <td align="center" valign="top">

            <div style="background-color: rgb(249, 250, 252);">
                
                <table class="rnb-del-min-width rnb-tmpl-width" width="100%" cellpadding="0" border="0" cellspacing="0" style="min-width:590px;" name="Layout_4" id="Layout_4">
                    <tbody><tr>
                        <td class="rnb-del-min-width" align="center" valign="top" style="min-width:590px;">
                            <table width="100%" cellpadding="0" border="0" align="center" cellspacing="0" bgcolor="#f9fafc" style="padding-right: 20px; padding-left: 20px; background-color: rgb(249, 250, 252);">
                                <tbody><tr>
                                    <td height="20" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td style="font-size:14px; color:#888888; font-weight:normal; text-align:center; font-family:Arial,Helvetica,sans-serif;">
                                        <div>© 2019 Beatbot.io</div>
                                    </td></tr>
                                <tr>
                                    <td height="20" style="font-size:1px; line-height:0px; mso-hide: all;">&nbsp;</td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                </tbody></table>
                
            </div></td>
    </tr></tbody></table>
            <!--[if gte mso 9]>
                        </td>
                        </tr>
                        </table>
                        <![endif]-->
                        </td>
        </tr>
        </tbody></table>

</body></html>
"""