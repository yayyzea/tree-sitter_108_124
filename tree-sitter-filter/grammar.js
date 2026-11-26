/**
 * @file Parser bahasa filter sederhana untuk membuat aturan penyaringan data.
 * @author Kayla & Zahra <kaylamutiara1206@gmail.com & azkiyaz65@gmail.com>
 * @license MIT
 */

/// <reference types="tree-sitter-cli/dsl" />
// @ts-check

export default grammar({
  name: 'filter',

  extras: $ => [/\s/],

  rules: {
    query: $ => repeat1($._expr),

    _expr: $ => choice(
      $.comparison,
      $.and_expression,
      $.or_expression,
      $.parenthesized_expression,
      $.not_expression,
      $.in_expression,
      $.contains_expression
    ),

    and_expression: $ => prec.left(2, seq(
      $._expr,
      'and',
      $._expr
    )),

    or_expression: $ => prec.left(1, seq(
      $._expr,
      'or',
      $._expr
    )),

    parenthesized_expression: $ => seq(
      '(',
      $._expr,
      ')'
    ),

    not_expression: $ => prec(3, seq(
      'not',
      $._expr
    )),

    comparison: $ => seq(
      field('field', $.identifier),
      field('operator', choice('=', '!=', '>', '<', '>=', '<=')),
      field('value', choice($.string, $.number, $.boolean))
    ),

    in_expression: $ => seq(
      $.identifier,
      'in',
      '(',
      $.string,
      repeat(seq(',', $.string)),
      ')'
    ),

    contains_expression: $ => seq(
      $.identifier,
      'contains',
      $.string
    ),

    identifier: $ => /[a-zA-Z_][a-zA-Z0-9_.]*/,

    string: $ => /"[^"]*"/,
    number: $ => /\d+/,
    word: $ => $.identifier,
    boolean: $ => choice('true', 'false'),
  }
});