# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device kltechnduo
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy S5 LTE

# Community HW adaptations need this
%define community_adaptation 1

# Sailfish OS is considered to-scale, if in app grid you get 4-in-a-row icons
# and 2x2 or 3x3 covers when up-to-4 or 5-or-more apps are open respectively.
# For 4-5.5" device screen sizes of 16:9 ratio, use this formula (hold portrait):
# pixel_ratio = 4.5/DiagonalDisplaySizeInches * HorizontalDisplayResolution/540
# Other screen sizes and ratios will require more trial-and-error.
%define pixel_ratio 1.0


%define straggler_files \
/bugreports \
/d \
/file_contexts.bin \
/property_contexts \
/sdcard \
/selinux_version \
/service_contexts \
/vendor \
/usr/bin/test_hwc2 \
/usr/include/hybris/hwc2/hwc2_compatibility_layer.h \
/usr/lib/libgralloc.so \
/usr/lib/libgralloc.so.1 \
/usr/lib/libgralloc.so.1.0.0 \
/usr/lib/libhwc2.so \
/usr/lib/libhwc2.so.1 \
/usr/lib/libhwc2.so.1.0.0 \
/usr/lib/pkgconfig/libgralloc.pc \
/usr/lib/pkgconfig/libhwc2.pc \
%{nil}


%include droid-configs-device/droid-configs.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

