#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.67])
AC_INIT([cputool], [0.0.8-1], [nkukard@lbsd.net])
AM_INIT_AUTOMAKE([-Wno-portability])

AC_CONFIG_SRCDIR([cputool.h])
AC_CONFIG_HEADERS([config.h])


# Checks for programs.
AC_PROG_CC_STDC
AC_GNU_SOURCE

# Checks for libraries.
AC_CHECK_LIB([rt], [fabs])

# Checks for header files.
AC_CHECK_HEADERS([fcntl.h stdint.h stdlib.h string.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_C_INLINE
AC_TYPE_PID_T
AC_TYPE_SSIZE_T
AC_TYPE_UINT32_T
AC_TYPE_UINT64_T

# Checks for library functions.
AC_FUNC_FORK
AC_FUNC_MALLOC
AC_FUNC_STRTOD
AC_CHECK_FUNCS([clock_gettime strerror])

AC_CHECK_PROGS(DOCBOOKTOMAN, docbook-to-man docbook2man, [no],)
if test x"$DOCBOOKTOMAN" = xno
then
	AC_MSG_WARN([docbook2man not found])
	# fail with a meaningfull error if $DOCBOOKTOMAN called by the makefile
	DOCBOOKTOMAN=docbook2man
fi

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
