# Starlette-WTF Changelog

# 0.4.1 - May 6, 2021

* Fixed issue with @csrf_protect decorator when applied to a function without a
  Request argument

# 0.4.0 - May 5, 2021

* Added support for class-based-views to @csrf_protect decorator

# 0.2.2 - February 3, 2020

* Added support for Starlette Secret datatypes when used for CSRF signing keys

# 0.2.1 - February 3, 2020

* Added CSRFProtectMiddleware configuration options to README
