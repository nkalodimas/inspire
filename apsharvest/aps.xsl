<?xml version="1.0" encoding="UTF-8"?>
<!--
This file was generated by Altova MapForce 2011r2

YOU SHOULD NOT MODIFY THIS FILE, BECAUSE IT WILL BE
OVERWRITTEN WHEN YOU RE-RUN CODE GENERATION.

Refer to the Altova MapForce Documentation for further details.
http://www.altova.com/mapforce
-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions" exclude-result-prefixes="xs fn">
   <xsl:output method="xml" encoding="UTF-8" indent="yes"/>
   <xsl:template match="/">
      <xsl:for-each select="article">
         <xsl:variable name="var1_meta" as="node()" select="meta"/>
         <xsl:for-each select="$var1_meta/doi/node()[fn:boolean(self::text())]">
            <xsl:variable name="var2_" as="xs:string" select="'7'"/>
            <xsl:variable name="var3_" as="xs:string" select="''"/>
            <xsl:variable name="var4_APS" as="xs:string" select="'APS'"/>
            <xsl:variable name="var5_resultof_create_attribute_with_prefix" as="node()">
               <xsl:attribute name="code" select="'c'"/>
            </xsl:variable>
            <xsl:variable name="var6_resultof_create_attribute_with_prefix" as="node()">
               <xsl:attribute name="code" select="'2'"/>
            </xsl:variable>
            <xsl:variable name="var7_resultof_create_attribute_with_prefix" as="node()">
               <xsl:attribute name="ind1" select="$var3_"/>
            </xsl:variable>
            <xsl:variable name="var8_resultof_create_attribute_with_prefix" as="node()">
               <xsl:attribute name="ind2" select="$var3_"/>
            </xsl:variable>
            <xsl:variable name="var9_resultof_create_attribute_with_prefix" as="node()">
               <xsl:attribute name="code" select="'a'"/>
            </xsl:variable>
            <xsl:variable name="var10_history" as="node()?" select="$var1_meta/history"/>
            <xsl:variable name="var11_authgrp" as="node()+" select="$var1_meta/authgrp"/>
            <xsl:variable name="var40_resultof_create_element_with_prefix" as="node()">
               <collection xmlns="http://www.loc.gov/MARC21/slim">
                  <xsl:attribute name="xsi:schemaLocation" namespace="http://www.w3.org/2001/XMLSchema-instance" select="'http://www.loc.gov/MARC21/slim //win.desy.de/home/sachs/MYDOCU~1/Altova/marcxml.xsd'"/>
                  <record>
                     <datafield>
                        <xsl:attribute name="tag" namespace="" select="'024'"/>
                        <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                        <xsl:attribute name="ind1" namespace="" select="$var2_"/>
                        <subfield>
                           <xsl:sequence select="($var6_resultof_create_attribute_with_prefix, 'DOI')"/>
                        </subfield>
                        <subfield>
                           <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, fn:string(.))"/>
                        </subfield>
                     </datafield>
                     <xsl:for-each select="$var11_authgrp">
                        <xsl:variable name="var25_cur" as="node()" select="."/>
                        <xsl:variable name="var24_idx" as="xs:integer" select="position()"/>
                        <xsl:for-each select="*:author[fn:namespace-uri() eq '']">
                           <xsl:variable name="var23_cur" as="node()" select="."/>
                           <xsl:variable name="var22_idx" as="xs:integer" select="position()"/>
                           <xsl:for-each select="*:surname[fn:namespace-uri() eq ''][(($var24_idx = xs:decimal('1')) and ($var22_idx = xs:decimal('1')))]">
                              <datafield>
                                 <xsl:attribute name="tag" namespace="" select="'100'"/>
                                 <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                                 <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                                 <xsl:for-each select="node()">
                                    <xsl:variable name="var21_cur" as="node()" select="."/>
                                    <xsl:if test="fn:boolean(self::text())">
                                       <xsl:for-each select="$var23_cur/*:givenname[fn:namespace-uri() eq '']/node()[fn:boolean(self::text())]">
                                          <xsl:variable name="var12_middlename" as="node()*" select="$var23_cur/*:middlename[fn:namespace-uri() eq '']"/>
                                          <xsl:variable name="var13_resultof_exists" as="xs:boolean" select="fn:exists($var12_middlename)"/>
                                          <xsl:variable name="var20_result" as="xs:boolean">
                                             <xsl:choose>
                                                <xsl:when test="$var13_resultof_exists">
                                                   <xsl:variable name="var15_result" as="xs:boolean*">
                                                      <xsl:for-each select="$var12_middlename">
                                                         <xsl:variable name="var14_result" as="xs:boolean*">
                                                            <xsl:for-each select="node()">
                                                               <xsl:sequence select="fn:boolean(self::text())"/>
                                                            </xsl:for-each>
                                                         </xsl:variable>
                                                         <xsl:sequence select="fn:exists($var14_result[.])"/>
                                                      </xsl:for-each>
                                                   </xsl:variable>
                                                   <xsl:sequence select="fn:exists($var15_result[.])"/>
                                                </xsl:when>
                                                <xsl:otherwise>
                                                   <xsl:sequence select="fn:true()"/>
                                                </xsl:otherwise>
                                             </xsl:choose>
                                          </xsl:variable>
                                          <xsl:if test="$var20_result">
                                             <xsl:variable name="var19_result" as="xs:string">
                                                <xsl:choose>
                                                   <xsl:when test="$var13_resultof_exists">
                                                      <xsl:variable name="var17_result" as="xs:boolean*">
                                                         <xsl:for-each select="$var12_middlename">
                                                            <xsl:variable name="var16_result" as="xs:boolean*">
                                                               <xsl:for-each select="node()">
                                                                  <xsl:sequence select="fn:boolean(self::text())"/>
                                                               </xsl:for-each>
                                                            </xsl:variable>
                                                            <xsl:sequence select="fn:exists($var16_result[.])"/>
                                                         </xsl:for-each>
                                                      </xsl:variable>
                                                      <xsl:if test="fn:exists($var17_result[.])">
                                                         <xsl:variable name="var18_result" as="xs:string*">
                                                            <xsl:for-each select="$var12_middlename/node()[fn:boolean(self::text())]">
                                                               <xsl:sequence select="fn:concat(' ', fn:string(.))"/>
                                                            </xsl:for-each>
                                                         </xsl:variable>
                                                         <xsl:sequence select="xs:string(fn:string-join(for $x in $var18_result return xs:string($x), ' '))"/>
                                                      </xsl:if>
                                                   </xsl:when>
                                                   <xsl:otherwise>
                                                      <xsl:sequence select="$var3_"/>
                                                   </xsl:otherwise>
                                                </xsl:choose>
                                             </xsl:variable>
                                             <subfield>
                                                <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, fn:concat(fn:concat(fn:string($var21_cur), ', '), replace(fn:concat(fn:string(.), $var19_result), '\. ', '.')))"/>
                                             </subfield>
                                          </xsl:if>
                                       </xsl:for-each>
                                    </xsl:if>
                                 </xsl:for-each>
                                 <xsl:for-each select="$var25_cur/*:aff[fn:namespace-uri() eq '']">
                                    <subfield>
                                       <xsl:attribute name="code" namespace="" select="'u'"/>
                                       <xsl:sequence select="fn:string(.)"/>
                                    </subfield>
                                 </xsl:for-each>
                              </datafield>
                           </xsl:for-each>
                        </xsl:for-each>
                     </xsl:for-each>
                     <datafield>
                        <xsl:attribute name="tag" namespace="" select="'245'"/>
                        <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                        <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                        <subfield>
                           <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, fn:string($var1_meta/*:title[fn:namespace-uri() eq '']))"/>
                        </subfield>
                     </datafield>
                     <xsl:for-each select="$var10_history/*:published[fn:namespace-uri() eq '']">
                        <datafield>
                           <xsl:attribute name="tag" namespace="" select="'260'"/>
                           <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                           <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                           <subfield>
                              <xsl:sequence select="($var5_resultof_create_attribute_with_prefix, fn:string(@date))"/>
                           </subfield>
                           <subfield>
                              <xsl:attribute name="code" namespace="" select="'t'"/>
                              <xsl:sequence select="'published'"/>
                           </subfield>
                        </datafield>
                     </xsl:for-each>
                     <xsl:for-each select="$var1_meta/*:numpages[fn:namespace-uri() eq '']">
                        <datafield>
                           <xsl:attribute name="tag" namespace="" select="'300'"/>
                           <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                           <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                           <xsl:for-each select="node()[fn:boolean(self::text())]">
                              <subfield>
                                 <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, fn:string(.))"/>
                              </subfield>
                           </xsl:for-each>
                        </datafield>
                     </xsl:for-each>
                     <xsl:for-each select="$var1_meta/*:abstract[fn:namespace-uri() eq '']">
                        <datafield>
                           <xsl:attribute name="tag" namespace="" select="'520'"/>
                           <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                           <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                           <xsl:for-each select="*:p[fn:namespace-uri() eq '']">
                              <subfield>
                                 <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, fn:string(.))"/>
                              </subfield>
                           </xsl:for-each>
                           <subfield>
                              <xsl:attribute name="code" namespace="" select="'9'"/>
                              <xsl:sequence select="$var4_APS"/>
                           </subfield>
                        </datafield>
                     </xsl:for-each>
                     <xsl:for-each select="$var1_meta/*:pacs[fn:namespace-uri() eq '']/*:pacscode[fn:namespace-uri() eq '']">
                        <datafield>
                           <xsl:attribute name="tag" namespace="" select="'084'"/>
                           <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                           <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                           <subfield>
                              <xsl:sequence select="($var6_resultof_create_attribute_with_prefix, 'PACS')"/>
                           </subfield>
                           <xsl:for-each select="node()[fn:boolean(self::text())]">
                              <subfield>
                                 <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, fn:string(.))"/>
                              </subfield>
                           </xsl:for-each>
                        </datafield>
                     </xsl:for-each>
                     <xsl:for-each select="$var11_authgrp">
                        <xsl:variable name="var39_cur" as="node()" select="."/>
                        <xsl:variable name="var38_idx" as="xs:integer" select="position()"/>
                        <xsl:for-each select="*:author[fn:namespace-uri() eq '']">
                           <xsl:variable name="var37_cur" as="node()" select="."/>
                           <xsl:variable name="var36_idx" as="xs:integer" select="position()"/>
                           <xsl:for-each select="*:surname[fn:namespace-uri() eq ''][fn:not((($var38_idx = xs:decimal('1')) and ($var36_idx = xs:decimal('1'))))]">
                              <datafield>
                                 <xsl:attribute name="tag" namespace="" select="'700'"/>
                                 <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                                 <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                                 <xsl:for-each select="node()">
                                    <xsl:variable name="var35_cur" as="node()" select="."/>
                                    <xsl:if test="fn:boolean(self::text())">
                                       <xsl:for-each select="$var37_cur/*:givenname[fn:namespace-uri() eq '']/node()[fn:boolean(self::text())]">
                                          <xsl:variable name="var26_middlename" as="node()*" select="$var37_cur/*:middlename[fn:namespace-uri() eq '']"/>
                                          <xsl:variable name="var27_resultof_exists" as="xs:boolean" select="fn:exists($var26_middlename)"/>
                                          <xsl:variable name="var34_result" as="xs:boolean">
                                             <xsl:choose>
                                                <xsl:when test="$var27_resultof_exists">
                                                   <xsl:variable name="var29_result" as="xs:boolean*">
                                                      <xsl:for-each select="$var26_middlename">
                                                         <xsl:variable name="var28_result" as="xs:boolean*">
                                                            <xsl:for-each select="node()">
                                                               <xsl:sequence select="fn:boolean(self::text())"/>
                                                            </xsl:for-each>
                                                         </xsl:variable>
                                                         <xsl:sequence select="fn:exists($var28_result[.])"/>
                                                      </xsl:for-each>
                                                   </xsl:variable>
                                                   <xsl:sequence select="fn:exists($var29_result[.])"/>
                                                </xsl:when>
                                                <xsl:otherwise>
                                                   <xsl:sequence select="fn:true()"/>
                                                </xsl:otherwise>
                                             </xsl:choose>
                                          </xsl:variable>
                                          <xsl:if test="$var34_result">
                                             <xsl:variable name="var33_result" as="xs:string">
                                                <xsl:choose>
                                                   <xsl:when test="$var27_resultof_exists">
                                                      <xsl:variable name="var31_result" as="xs:boolean*">
                                                         <xsl:for-each select="$var26_middlename">
                                                            <xsl:variable name="var30_result" as="xs:boolean*">
                                                               <xsl:for-each select="node()">
                                                                  <xsl:sequence select="fn:boolean(self::text())"/>
                                                               </xsl:for-each>
                                                            </xsl:variable>
                                                            <xsl:sequence select="fn:exists($var30_result[.])"/>
                                                         </xsl:for-each>
                                                      </xsl:variable>
                                                      <xsl:if test="fn:exists($var31_result[.])">
                                                         <xsl:variable name="var32_result" as="xs:string*">
                                                            <xsl:for-each select="$var26_middlename/node()[fn:boolean(self::text())]">
                                                               <xsl:sequence select="fn:concat(' ', fn:string(.))"/>
                                                            </xsl:for-each>
                                                         </xsl:variable>
                                                         <xsl:sequence select="xs:string(fn:string-join(for $x in $var32_result return xs:string($x), ' '))"/>
                                                      </xsl:if>
                                                   </xsl:when>
                                                   <xsl:otherwise>
                                                      <xsl:sequence select="$var3_"/>
                                                   </xsl:otherwise>
                                                </xsl:choose>
                                             </xsl:variable>
                                             <subfield>
                                                <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, fn:concat(fn:concat(fn:string($var35_cur), ', '), replace(fn:concat(fn:string(.), $var33_result), '\. ', '.')))"/>
                                             </subfield>
                                          </xsl:if>
                                       </xsl:for-each>
                                    </xsl:if>
                                 </xsl:for-each>
                                 <xsl:for-each select="$var39_cur/*:aff[fn:namespace-uri() eq '']">
                                    <subfield>
                                       <xsl:attribute name="code" namespace="" select="'u'"/>
                                       <xsl:sequence select="fn:string(.)"/>
                                    </subfield>
                                 </xsl:for-each>
                              </datafield>
                           </xsl:for-each>
                        </xsl:for-each>
                     </xsl:for-each>
                     <datafield>
                        <xsl:attribute name="tag" namespace="" select="'773'"/>
                        <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                        <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                        <xsl:for-each select="$var1_meta/*:eid[fn:namespace-uri() eq '']/node()[fn:boolean(self::text())]">
                           <subfield>
                              <xsl:sequence select="($var5_resultof_create_attribute_with_prefix, fn:string(.))"/>
                           </subfield>
                        </xsl:for-each>
                        <xsl:for-each select="$var1_meta/*:issue[fn:namespace-uri() eq '']/node()[fn:boolean(self::text())]">
                           <subfield>
                              <xsl:attribute name="code" namespace="" select="'n'"/>
                              <xsl:sequence select="fn:string(.)"/>
                           </subfield>
                        </xsl:for-each>
                        <xsl:for-each select="$var1_meta/*:journal[fn:namespace-uri() eq '']/node()[fn:boolean(self::text())]">
                           <subfield>
                              <xsl:attribute name="code" namespace="" select="'p'"/>
                              <xsl:sequence select="fn:string(.)"/>
                           </subfield>
                        </xsl:for-each>
                        <xsl:for-each select="$var1_meta/*:volume[fn:namespace-uri() eq '']/node()[fn:boolean(self::text())]">
                           <subfield>
                              <xsl:attribute name="code" namespace="" select="'v'"/>
                              <xsl:sequence select="fn:string(.)"/>
                           </subfield>
                        </xsl:for-each>
                        <xsl:for-each select="$var10_history/*:published[fn:namespace-uri() eq '']">
                           <subfield>
                              <xsl:attribute name="code" namespace="" select="'y'"/>
                              <xsl:sequence select="replace(fn:string(@date), '-.*', '')"/>
                           </subfield>
                        </xsl:for-each>
                     </datafield>
                     <datafield>
                        <xsl:attribute name="tag" namespace="" select="'541'"/>
                        <xsl:sequence select="$var8_resultof_create_attribute_with_prefix"/>
                        <xsl:sequence select="$var7_resultof_create_attribute_with_prefix"/>
                        <subfield>
                           <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, $var4_APS)"/>
                        </subfield>
                        <subfield>
                           <xsl:sequence select="($var5_resultof_create_attribute_with_prefix, 'batchupload')"/>
                        </subfield>
                     </datafield>
                     <xsl:for-each select="$var1_meta/*:tocsec[fn:namespace-uri() eq '']">
                        <datafield>
                           <xsl:attribute name="tag" namespace="" select="'650'"/>
                           <xsl:attribute name="ind2" namespace="" select="$var2_"/>
                           <xsl:attribute name="ind1" namespace="" select="'1'"/>
                           <xsl:for-each select="node()[fn:boolean(self::text())]">
                              <subfield>
                                 <xsl:sequence select="($var9_resultof_create_attribute_with_prefix, fn:string(.))"/>
                              </subfield>
                           </xsl:for-each>
                           <subfield>
                              <xsl:sequence select="($var6_resultof_create_attribute_with_prefix, $var4_APS)"/>
                           </subfield>
                        </datafield>
                     </xsl:for-each>
                  </record>
               </collection>
            </xsl:variable>
            <xsl:result-document href="{fn:concat(replace(fn:string(.), '[/()]', '_'), '.xml')}" encoding="UTF-8">
               <xsl:sequence select="$var40_resultof_create_element_with_prefix"/>
            </xsl:result-document>
         </xsl:for-each>
      </xsl:for-each>
   </xsl:template>
</xsl:stylesheet>
