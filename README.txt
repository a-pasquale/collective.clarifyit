.. contents::

Introduction
============

This product integrates Clarify-It.com documents into Plone.  

The product adds a "Clarify It" content type to Plone which allows you to enter the Clarify-It document ID.  This document is loaded using jQuery.load() call.  The clarify-it.com domain is currently hard-coded into the view and should be changed to your own url.  

This product relies on nginx proxy_pass and rewriting to bypass the browser's cross domain scripting restrictions.  Put something like this in your nginx configuration:

location /clarify {                
    rewrite             /clarify/(.*) /d/$1 break;
    proxy_pass http://healthlens.clarify-it.com/;
    proxy_set_header    Host        healthlens.clarify-it.com;
    proxy_set_header    X-Real-IP   $remote_addr;               
    proxy_set_header    X-Forwarded-For     $remote_addr;
    proxy_set_header    X-Originating-IP    $remote_addr;
    proxy_set_header    HTTP_REMOTE_ADDR    $remote_addr;
    proxy_set_header    REMOTE_ADDR         $remote_addr;
}

The product has a dependency on collective.prettyphoto for image overlays.
